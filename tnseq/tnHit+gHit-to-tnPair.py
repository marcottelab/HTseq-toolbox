#!/usr/bin/env python
import os
import sys
import gzip
import re

filename_tnHit = sys.argv[1]
filename_base = filename_tnHit.replace('_tnHit','')
filename_gHit = filename_base+'_gHit'
if( len(sys.argv) > 2 ):
    filename_gHit = sys.argv[2]

pair2reads = dict()
multi_hits = dict()
tn_hits = dict()
g_hits = dict()

p_hit = re.compile(r'[ATGC]{10,}')

sys.stderr.write('Read %s ... '%filename_tnHit)
f_tnHit = open(filename_tnHit,'r')
if( filename_tnHit.endswith('.gz') ):
    f_tnHit = gzip.open(filename_tnHit,'rb')

for line in f_tnHit:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    read_id = tokens[0]
    hit_strand = tokens[1]
    hit_start = int(tokens[2])
    hit_end = int(tokens[3])
    read_seq = tokens[4]
    if( tn_hits.has_key(read_id) ):
        multi_hits[read_id] = 1 
        continue
    
    tn_hits[read_id] = {'start':hit_start, 'end':hit_end, 'strand':hit_strand, 'read_seq':read_seq}
    pair_id = read_id.split('/')[0]
    if( not pair2reads.has_key(pair_id) ):
        pair2reads[pair_id] = []
    pair2reads[pair_id].append(read_id)
f_tnHit.close()
sys.stderr.write('Done\n')

sys.stderr.write('Read %s ... '%filename_gHit)
f_gHit = open(filename_gHit,'r')
if( filename_gHit.endswith('.gz') ):
    f_gHit = gzip.open(filename_gHit,'rb')

for line in f_gHit:
    tokens = line.strip().split("\t")
    read_id = tokens[0]
    hit_strand = tokens[1]
    hit_start = int(tokens[2])
    hit_end = int(tokens[3])
    read_seq = tokens[4]
    if( tn_hits.has_key(read_id) ):
        multi_hits[read_id] = 1 
        continue
    
    pair_id = read_id.split('/')[0]
    if( not pair2reads.has_key(pair_id) ):
        continue
    pair2reads[pair_id].append(read_id)
    g_hits[read_id] = {'start':hit_start, 'end':hit_end, 'strand':hit_strand, 'read_seq':read_seq}
f_gHit.close()
sys.stderr.write('Done\n')

f_both = open('%s_tnPairTT'%filename_base,'w')
f_single = open('%s_tnPairTG'%filename_base,'w')
for tmp_p in sorted(pair2reads.keys()):
    tmp_read_list = list(set(pair2reads[tmp_p]))
    if( len(tmp_read_list) != 2 ):
        ## Single hit
        continue

    tmp_r1 = tmp_read_list[0]
    tmp_r2 = tmp_read_list[1]
    if( tn_hits.has_key(tmp_r1) and tn_hits.has_key(tmp_r2) ):
        tmp_h1 = tn_hits[tmp_r1]
        tmp_h2 = tn_hits[tmp_r2]
        if( tmp_h1['start'] > tmp_h2['start'] ):
            tmp_h = tmp_h1
            tmp_h1 = tmp_h2
            tmp_h2 = tmp_h
        f_both.write('%s\t%d|%d|%s\t%d|%d|%s\t%s\t%s\n'%(tmp_p,tmp_h1['start'],tmp_h1['end'],tmp_h1['strand'],tmp_h2['start'],tmp_h2['end'],tmp_h2['strand'],tmp_h1['read_seq'],tmp_h2['read_seq']))

    elif( tn_hits.has_key(tmp_r1) and g_hits.has_key(tmp_r2) ):
        tmp_h1 = tn_hits[tmp_r1]
        tmp_h2 = g_hits[tmp_r2]
        if( tmp_h1['start'] > tmp_h2['start'] ):
            tmp_h = tmp_h1
            tmp_h1 = tmp_h2
            tmp_h2 = tmp_h
        f_single.write('%s\t%d|%d|%s\t%d|%d|%s\t%s\t%s\n'%(tmp_p,tmp_h1['start'],tmp_h1['end'],tmp_h1['strand'],tmp_h2['start'],tmp_h2['end'],tmp_h2['strand'],tmp_h1['read_seq'],tmp_h2['read_seq']))

    elif( g_hits.has_key(tmp_r1) and tn_hits.has_key(tmp_r2) ):
        tmp_h1 = g_hits[tmp_r1]
        tmp_h2 = tn_hits[tmp_r2]
        if( tmp_h1['start'] > tmp_h2['start'] ):
            tmp_h = tmp_h1
            tmp_h1 = tmp_h2
            tmp_h2 = tmp_h
        f_single.write('%s\t%d|%d|%s\t%d|%d|%s\t%s\t%s\n'%(tmp_p,tmp_h1['start'],tmp_h1['end'],tmp_h1['strand'],tmp_h2['start'],tmp_h2['end'],tmp_h2['strand'],tmp_h1['read_seq'],tmp_h2['read_seq']))
f_single.close()
f_both.close()
