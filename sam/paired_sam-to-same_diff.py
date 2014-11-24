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

for line in f_sam:
    if( line.startswith('@') and len(line.split()[0]) < 4 ):
        f_same.write(line)
        f_diff.write(line)
        continue
    tokens = line.strip().split("\t")
    t1_id = tokens[2]
    t2_id = tokens[6]
    if( t1_id == '*' ):
        f_nohit.write(line)
        continue

    if( t2_id == '=' ):
        t1_pos = int(tokens[3])
        t2_pos = int(tokens[7])
        if( t1_pos == t2_pos ):
            f_unpaired.write(line)
        else:
            f_same.write(line)
    elif( t2_id != '*' ):
        f_diff.write(line)
f_sam.close()

f_same.close()
f_diff.close()
f_nohit.close()
f_unpaired.close()
