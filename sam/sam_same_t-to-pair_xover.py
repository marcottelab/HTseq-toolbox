#!/usr/bin/env python
import os
import sys
import math
import re

filename_sam = sys.argv[1]
filename_out = re.sub(r'.sam[_A-z]*$','',filename_sam) + '.pair_xover'
sys.stderr.write('%s -> %s\n'%(filename_sam, filename_out))

step_size = 1000

#min_dist = 500
#max_dist = 500000
exp_dist = 10000
min_dist = exp_dist*0.1
max_dist = exp_dist*1.9

t2pair = dict()
pair_freq = dict()
pair_dist = []
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
    tmp_dist = abs(t2_pos - t1_pos)

    if( not pair_freq.has_key(pair_id) ):
        pair_freq[pair_id] = 0
    pair_freq[pair_id] += 1
    if( not t2pair.has_key(t1_id) ):
        t2pair[t1_id] = dict()
    if( not t2pair[t1_id].has_key(pair_id) ):
        t2pair[t1_id][pair_id] = []

    t2pair[t1_id][pair_id].append( sorted([t1_pos, t2_pos]))
    pair_dist.append( tmp_dist )
f_sam.close()

pair_dist = sorted([x for x in pair_dist if x > exp_dist*0.1])
Q50_dist = pair_dist[ int(len(pair_dist)*0.50) ]
Q25_dist = pair_dist[ int(len(pair_dist)*0.25) ]
Q75_dist = pair_dist[ int(len(pair_dist)*0.75) ]
IQR = Q75_dist - Q25_dist

sys.stderr.write('%s - median_dist:%d, IQR:%d\n'%(filename_out, Q50_dist, IQR))

#import matplotlib.pyplot as plt
#fig = plt.figure(figsize=(8,8))
#ax1 = fig.add_subplot(1,1,1)
#ax1.hist(pair_dist, bins=range(100,20000,100))
#plt.show()

pair_pos = dict()
long_pos = dict()
short_pos = dict()
for tmp_t_id in t2pair.keys():
    pair_pos[tmp_t_id] = dict()
    long_pos[tmp_t_id] = dict()
    short_pos[tmp_t_id] = dict()

    for tmp_pair in t2pair[tmp_t_id].keys():
        if( pair_freq[tmp_pair] > 2 ):
            continue

        for tmp_pos1, tmp_pos2 in t2pair[tmp_t_id][tmp_pair]:
            tmp_dist = tmp_pos2 - tmp_pos1
            #if( tmp_dist < Q50_dist-1.5*IQR ):
            if( tmp_dist < Q25_dist ):
                short_pos[tmp_t_id][tmp_pos1] = tmp_pos2
            #elif( tmp_dist > Q50_dist+1.5*IQR ):
            elif( tmp_dist > Q75_dist ):
                long_pos[tmp_t_id][tmp_pos1] = tmp_pos2
            else:
                pair_pos[tmp_t_id][tmp_pos1] = tmp_pos2

f_out = open(filename_out,'w')
f_out.write('#TargetID\tPos\tPairFreq\tLongFreq\tShortFreq\n')
f_out.write('#Median:%d Q25:%d Q75:%d IQR:%d\n'%(Q50_dist,Q25_dist,Q75_dist,IQR))
for tmp_t_id in pair_pos.keys():
    if( not seqlen.has_key(tmp_t_id) ):
        continue
    
    tmp_freq = dict()
    dist_list = []
    for tmp_pos in range(0,seqlen[tmp_t_id],step_size):
        tmp_freq[tmp_pos] = {'pair':0, 'long':0, 'short':0}
    
    for tmp_start_pos in pair_pos[tmp_t_id].keys():
        tmp_end_pos = pair_pos[tmp_t_id][tmp_start_pos]
        for tmp_pos in range(int(tmp_start_pos/step_size), int(tmp_end_pos/step_size)+1):
            tmp_pos = tmp_pos * step_size
            tmp_freq[tmp_pos]['pair'] += 1
            #dist_list.append( tmp_end_pos - tmp_start_pos )

    for tmp_start_pos in long_pos[tmp_t_id].keys():
        tmp_end_pos = long_pos[tmp_t_id][tmp_start_pos]
        for tmp_pos in range(int(tmp_start_pos/step_size), int(tmp_end_pos/step_size)+1):
            tmp_pos = tmp_pos * step_size
            tmp_freq[tmp_pos]['long'] += 1

    for tmp_start_pos in short_pos[tmp_t_id].keys():
        tmp_end_pos = short_pos[tmp_t_id][tmp_start_pos]
        for tmp_pos in range(int(tmp_start_pos/step_size), int(tmp_end_pos/step_size)+1):
            tmp_pos = tmp_pos * step_size
            tmp_freq[tmp_pos]['short'] += 1
    
    for tmp_pos in range(0,seqlen[tmp_t_id],step_size):
        f_out.write("%s\t%d\t%d\t%d\t%d\n"%(tmp_t_id, tmp_pos, tmp_freq[tmp_pos]['pair'], tmp_freq[tmp_pos]['long'], tmp_freq[tmp_pos]['short']))
f_out.close()
