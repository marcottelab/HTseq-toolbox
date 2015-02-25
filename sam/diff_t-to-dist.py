#!/usr/bin/env python
import os
import sys

filename_same_t = sys.argv[1]

f_t = open(filename_same_t,'r')
for line in f_t:
    tokens = line.strip().split("\t")
    if( line.startswith('@') and len(tokens) < 11 ):
        continue
    read_id = tokens[0]
    tmp_flag = tokens[1]
    t1_id = tokens[2]
    t1_pos = int(tokens[3])
    t2_id = tokens[6]
    t2_pos = int(tokens[7])
    tmp_dist = int(tokens[8])
    print "%s\t%s\t%s\t%d\t%s\t%d"%(read_id,tmp_flag, t1_id,t1_pos,t2_id, t2_pos)
f_t.close()
