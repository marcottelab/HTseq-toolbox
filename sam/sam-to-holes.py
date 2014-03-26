#!/usr/bin/env python
import os
import sys
import gzip

filename_sam = sys.argv[1]

seq_map = dict()
f_sam = open(filename_sam, 'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')

for line in f_sam:
    if( line.startswith('@') ):
        if( line.startswith('@SQ') ):
            tokens = line.strip().split()
            seq_map[ tokens[1].split(':')[1] ] = [0 for x in range(0, int(tokens[2].split(':')[1]))]
        continue

    tokens = line.strip().split("\t")
    t_id = tokens[2]
    t_pos = int(tokens[3])
    read_len = len(tokens[9])
    if( t_id == '*' ):
        continue

    for tmp_i in range(0,read_len):
        if( tmp_i+t_pos >= len(seq_map[t_id]) ):
            continue
        seq_map[t_id][tmp_i+t_pos] += 1
f_sam.close()

filename_base = filename_sam.replace('.sam','').replace('.sam_hit.gz','')

f_holes = open('%s.holes'%filename_base,'w')
f_holes100 = open('%s.holes100'%filename_base,'w')
f_holes.write('#TargetID\tGapStart\tGapEnd\tGapLen\n')
f_holes100.write('#TargetID\tGapStart\tGapEnd\tGapLen\n')

for t_id in seq_map.keys():
    start_list = []
    end_list = []
    for i in range(1,len(seq_map[t_id])):
        if( seq_map[t_id][i-1] == 0 and seq_map[t_id][i] > 0 ):
            end_list.append(i)
        elif( seq_map[t_id][i-1] > 0 and seq_map[t_id][i] == 0 ):
            start_list.append(i)

    for i in range(1,len(start_list)):
        tmp_diff = end_list[i+1] - start_list[i]
        
        f_holes.write("%s\t%d\t%d\t%d\n"%(t_id,start_list[i],end_list[i+1],tmp_diff))
        if( tmp_diff > 100 ):
            f_holes100.write("%s\t%d\t%d\t%d\n"%(t_id,start_list[i],end_list[i+1],tmp_diff))

f_holes.close()
f_holes100.close()
