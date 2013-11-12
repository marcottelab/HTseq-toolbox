#!/usr/bin/python
import os 
import sys

filename_best = sys.argv[1]
filename_part = filename_best.replace('_best','')+'_part'

f_part = open(filename_part,'w')
f_best = open(filename_best,'r')
for line in f_best:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    q_len = int(tokens[1])
    t_id = tokens[2]
    t_len = int(tokens[3])
    align_len = int(tokens[4])
    mismatches = int(tokens[5])
    gap_opens = int(tokens[6])
    bitscore = float(tokens[7])
    
    align_ratio = (align_len - mismatches)*100.0 / q_len
    if( gap_opens == 0 and align_ratio > 99 and q_len <= t_len ):
        f_part.write("%s\n"%(line.strip()))
f_best.close()
f_part.close()
