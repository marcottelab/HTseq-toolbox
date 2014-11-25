#!/usr/bin/env python
import os
import sys
import gzip
import re

filename_sam = sys.argv[1]
filename_base = filename_sam

f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')
    filename_base = re.sub(r'.gz$','',filename_base)

f_same = open('%s_same_t'%filename_base,'w')
f_diff = open('%s_diff_t'%filename_base,'w')
f_nohit = open('%s_nohit_t'%filename_base,'w')
f_unpaired = open('%s_unpaired_t'%filename_base,'w')

count_same = 0
count_diff = 0
count_nohit = 0
count_unpaired = 0

for line in f_sam:
    if( line.startswith('@') and len(line.split()[0]) < 4 ):
        f_same.write(line)
        f_diff.write(line)
        f_nohit.write(line)
        f_unpaired.write(line)
        continue

    tokens = line.strip().split("\t")
    t1_id = tokens[2]
    t2_id = tokens[6]
    if( t1_id == '*' ):
        f_nohit.write(line)
        count_nohit += 1
        continue

    if( t2_id == '=' ):
        t1_pos = int(tokens[3])
        t2_pos = int(tokens[7])
        if( t1_pos == t2_pos ):
            f_unpaired.write(line)
            count_unpaired += 1
        else:
            f_same.write(line)
            count_same += 1
    elif( t2_id != '*' ):
        f_diff.write(line)
        count_diff += 1
f_sam.close()

sys.stderr.write('%s - same:%d, diff:%d, nohit:%d, unpaired:%d\n'%(filename_sam, count_same, count_diff, count_nohit, count_unpaired))
f_same.close()
f_diff.close()
f_nohit.close()
f_unpaired.close()
