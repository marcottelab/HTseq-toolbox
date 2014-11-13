#!/usr/bin/env python
import os
import sys
import gzip
import re

filename_psl = sys.argv[1]
filename_out = re.sub(r'psl(.gz)*$','',filename_psl) + 'pair_xover'
sys.stderr.write('%s -> %s\n'%(filename_psl, filename_out))

step_size = 1000
min_dist = 500
max_dist = 500000

t2pair = dict()
f_psl = open(filename_psl,'r')
if( filename_psl.endswith('.gz') ):
    f_psl = gzip.open(filename_psl,'rb')

#1098	24	0	0	7	8	11	12	-	XLB1-001A09.b	1195	65	1195	JGIv71.000040421	3234181	1913640	1914774	19	4,27,2,4,1,19,11,14,8,20,14,6,16,9,9,15,27,28,888,	0,5,32,34,38,39,58,69,84,93,113,128,135,151,162,171,186,214,242,	1913640,1913644,1913672,1913675,1913680,1913683,1913703,1913715,1913729,1913737,1913758,1913772,1913778,1913795,1913804,1913814,1913830,1913857,1913886,
sys.stderr.write("Read %s\n"%filename_psl)
for line in f_psl:
    tokens = line.strip().split("\t")
    if( not tokens[0].isdigit() ):
        continue

    tokens = line.strip().split("\t")
    align_len = int(tokens[0])
    q_id = tokens[9]
    pair_id = '.'.join(q_id.split('.')[:-1])
    q_len = int(tokens[10])
    t_id = tokens[13]
    t_len = int(tokens[14])
    t_pos = int(tokens[15])
    if( align_len < q_len * 0.5 ):
        continue

    if( not t2pair.has_key(t_id) ):
        t2pair[t_id] = dict()
    if( not t2pair[t_id].has_key(pair_id) ):
        t2pair[t_id][pair_id] = dict()
    t2pair[t_id][pair_id][t_pos] = 1
f_psl.close()

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

f_out = open(filename_out,'w')
for tmp_t_id in pair_dist.keys():
    if( len(pair_dist[tmp_t_id]) == 0 ):
        continue

    pos_list = sorted(pair_dist[tmp_t_id].keys())
    if( pos_list[-1] < step_size ):
        continue

    for tmp_pos in range(0,pos_list[-1],step_size):
        tmp_cross_freq = 0
        for tmp_start_pos in pair_dist[tmp_t_id].keys():
            tmp_end_pos = pair_dist[tmp_t_id][tmp_start_pos]
            if( tmp_pos > tmp_start_pos and tmp_pos < tmp_end_pos ):
                tmp_cross_freq += 1

        tmp_singleton_freq = 0 
        if( singleton_freq.has_key(tmp_t_id) and singleton_freq[tmp_t_id].has_key(tmp_pos) ):
            tmp_singleton_freq = singleton_freq[tmp_t_id][tmp_pos]
        f_out.write("%s\t%d\t%d\t%d\n"%(tmp_t_id, tmp_pos, tmp_cross_freq, tmp_singleton_freq)) 
f_out.close()
