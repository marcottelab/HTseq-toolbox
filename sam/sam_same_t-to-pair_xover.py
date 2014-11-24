#!/usr/bin/env python
import os
import sys
import re

filename_sam = sys.argv[1]
filename_out = re.sub(r'.sam[_A-z]*$','',filename_sam) + '.pair_xover'
sys.stderr.write('%s -> %s\n'%(filename_sam, filename_out))

step_size = 1000
min_dist = 500
#max_dist = 500000
max_dist = 15000

t2pair = dict()
pair_freq = dict()
seqlen = dict()
f_sam = open(filename_sam,'r')
sys.stderr.write("Read %s\n"%filename_sam)
for line in f_sam:
    if( line.startswith('@') ):
        #@SQ	SN:JGIv71.000089040	LN:4033529
        if( line.startswith('@SQ') and line.find('LN:') > 0 ):
            tmp_id, tmp_len = line.strip().split()[1:]
            tmp_id = re.sub(r'^SN:','',tmp_id)
            tmp_len = int(re.sub(r'^LN:','',tmp_len))
            seqlen[tmp_id] = tmp_len
        continue

    tokens = line.strip().split("\t")
    read_id = tokens[0]
    pair_id = read_id.split('/')[0]
    flag = tokens[1]
    t1_id = tokens[2]
    t1_pos = int(tokens[3])
    cigar1 = tokens[5]
    if( t1_id == '*' or cigar1 == '*' ):
        continue

    t2_id = tokens[6]
    t2_pos = int(tokens[7])
    ## only works with paired mapped SAM (memory issue)
    if( t2_id != '=' ):
        continue
    if( t1_pos == t2_pos ):
        continue

    if( not pair_freq.has_key(pair_id) ):
        pair_freq[pair_id] = 0
    pair_freq[pair_id] += 1
    if( not t2pair.has_key(t1_id) ):
        t2pair[t1_id] = dict()
    if( not t2pair[t1_id].has_key(pair_id) ):
        t2pair[t1_id][pair_id] = []
    t2pair[t1_id][pair_id].append( sorted([t1_pos, t2_pos]))
f_sam.close()

pair_dist = dict()
for tmp_t_id in t2pair.keys():
    pair_dist[tmp_t_id] = dict()

    for tmp_pair in t2pair[tmp_t_id].keys():
        if( pair_freq[tmp_pair] > 2 ):
            continue
        for tmp_pos1, tmp_pos2 in t2pair[tmp_t_id][tmp_pair]:
            tmp_dist = tmp_pos2 - tmp_pos1
            if( tmp_dist < min_dist or tmp_dist > max_dist ):
                continue
            pair_dist[tmp_t_id][tmp_pos1] = tmp_pos2

f_out = open(filename_out,'w')
for tmp_t_id in pair_dist.keys():
    if( not seqlen.has_key(tmp_t_id) ):
        continue
    
    print len(pair_dist[tmp_t_id])*1.0/seqlen[tmp_t_id]
    for tmp_pos in range(0,seqlen[tmp_t_id],step_size):
        tmp_cross_freq = 0

        dist_list = []
        for tmp_start_pos in pair_dist[tmp_t_id].keys():
            tmp_end_pos = pair_dist[tmp_t_id][tmp_start_pos]
            if( tmp_pos > tmp_start_pos and tmp_pos < tmp_end_pos ):
                tmp_cross_freq += 1
                dist_list.append( tmp_end_pos - tmp_start_pos )

        f_out.write("%s\t%d\t%d\t%s\n"%(tmp_t_id, tmp_pos, tmp_cross_freq, ','.join(['%d'%x for x in dist_list]))) 
f_out.close()
