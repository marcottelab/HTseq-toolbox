#!/usr/bin/python
import os
import sys

filename_sum = sys.argv[1]

sum_list = []

s_ratio_list = []
t1s_ratio_list = []
t1_ratio_list = []
t2_ratio_list = []
f_sum = open(filename_sum,'r')
for line in f_sum:
    tokens = line.strip().split("\t")
    sum_list.append(tokens)
    q_id = tokens[0]
    q_len = int(tokens[1])
    #if( q_len < 2000 ):
    #    continue
    t1_id = tokens[2]
    t1_ratio = float(tokens[4])
    t2_id = tokens[8]
    t2_ratio = float(tokens[10])
    t1s_ratio_list.append(t1_ratio)
    if( t2_id == 'NA' ):
        s_ratio_list.append(t1_ratio)
    else:
        t1_ratio_list.append(t1_ratio)
        t2_ratio_list.append(t2_ratio)
f_sum.close()

ratio_1pct = 0
ratio_5pct = 0
count_t1_1pct = 0 
count_t2_1pct = 0
#print "Single: ",len(t1_ratio_list) - len(t2_ratio_list)
for tmp_ratio in [x*0.01 for x in range(100,0,-1)]:
    t1s_count = len([x for x in t1s_ratio_list if x > tmp_ratio])
    t2_count = len([x for x in t2_ratio_list if x > tmp_ratio])
    if( t1s_count+t2_count == 0 ):
        continue
    tmp_t2_ratio = float(t2_count) / (t1s_count+t2_count)
    if( tmp_t2_ratio < 0.01 ):
        sys.stderr.write('Test ratio:%.2f, T2 ratio:%.3f, T1 count:%d, T2 count:%d\n'%(tmp_ratio, tmp_t2_ratio, t1s_count, t2_count))
        ratio_1pct = tmp_ratio
        count_t1_1pct = t1s_count
        count_t2_1pct = t2_count
    elif( tmp_t2_ratio < 0.05 ):
        sys.stderr.write('Test ratio:%.2f, T2 ratio:%.3f, T1 count:%d, T2 count:%d\n'%(tmp_ratio, tmp_t2_ratio, t1s_count, t2_count))
        ratio_5pct = tmp_ratio
        break

f_out = open('%s_1pct.txt'%filename_sum,'w')
for tmp_s in sum_list:
    tmp_t1_ratio = float(tmp_s[4])
    if( tmp_t1_ratio > ratio_1pct ):
        f_out.write('%s\n'%("\t".join(tmp_s)))
f_out.close()

f_out = open('%s_5pct.txt'%filename_sum,'w')
for tmp_s in sum_list:
    tmp_t1_ratio = float(tmp_s[4])
    if( tmp_t1_ratio > ratio_5pct ):
        f_out.write('%s\n'%("\t".join(tmp_s)))
f_out.close()

f_out = open('%s_080ratio.txt'%filename_sum,'w')
for tmp_s in sum_list:
    tmp_t1_ratio = float(tmp_s[4])
    if( tmp_t1_ratio > 0.80 ):
        f_out.write('%s\n'%("\t".join(tmp_s)))
f_out.close()
