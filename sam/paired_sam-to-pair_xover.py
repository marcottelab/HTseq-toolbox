#!/usr/bin/env python
import os
import sys
import re

filename_sam = sys.argv[1]
filename_out = re.sub(r'.sam[_A-z]*$','.pair_xover',filename_sam)
sys.stderr.write('%s -> %s\n'%(filename_sam, filename_out))

step_size = 1000
min_dist = 500
max_dist = 500000

t2pair = dict()
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
    t_id = tokens[2]
    t_pos = int(tokens[3])
    cigar = tokens[5]
    if( t_id == '*' or cigar == '*' ):
        continue

    tmp_AS = 0
    tmp_XS = 0
    for tmp in tokens[11:]:
        if( tmp.startswith('AS') ):
            tmp_AS = int(tmp.split(':')[2])
        if( tmp.startswith('XS') ):
            tmp_XS = int(tmp.split(':')[2])

    if( not t2pair.has_key(t_id) ):
        t2pair[t_id] = dict()
    if( not t2pair[t_id].has_key(pair_id) ):
        t2pair[t_id][pair_id] = dict()
    t2pair[t_id][pair_id][t_pos] = {'cigar':cigar, 'flag':flag, 'AS':tmp_AS, 'XS':tmp_XS}
f_sam.close()

singleton_freq = dict()
pair_dist = dict()
for tmp_t_id in t2pair.keys():
    singleton_freq[tmp_t_id] = dict()
    pair_dist[tmp_t_id] = dict()

    for tmp_pair in t2pair[tmp_t_id].keys():
        tmp_pos_list = sorted(t2pair[tmp_t_id][tmp_pair].keys())
        if( len(tmp_pos_list) == 1 ):
            tmp_pos_idx = int(tmp_pos_list[0]/step_size)*step_size
            if( not singleton_freq[tmp_t_id].has_key(tmp_pos_idx) ):
                singleton_freq[tmp_t_id][tmp_pos_idx] = 0
            singleton_freq[tmp_t_id][tmp_pos_idx] += 1
            continue

        elif( len(tmp_pos_list) == 2 ):
            tmp_dist = tmp_pos_list[1] - tmp_pos_list[0]
            if( tmp_dist < min_dist or tmp_dist > max_dist ):
                continue
            pair_dist[tmp_t_id][tmp_pos_list[0]] = tmp_pos_list[1]

for tmp_t_id in pair_dist.keys():
    if( not seqlen.has_key(tmp_t_id) ):
        continue
    for tmp_pos in range(0,seqlen[tmp_t_id],step_size):
        tmp_cross_freq = 0
        for tmp_start_pos in pair_dist[tmp_t_id].keys():
            tmp_end_pos = pair_dist[tmp_t_id][tmp_start_pos]
            if( tmp_pos > tmp_start_pos and tmp_pos < tmp_end_pos ):
                tmp_cross_freq += 1

        tmp_singleton_freq = 0 
        if( singleton_freq.has_key(tmp_t_id) and singleton_freq[tmp_t_id].has_key(tmp_pos) ):
            tmp_singleton_freq = singleton_freq[tmp_t_id][tmp_pos]
        print "%s\t%d\t%d\t%d"%(tmp_t_id, tmp_pos, tmp_cross_freq, tmp_singleton_freq) 
