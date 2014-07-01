#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        tmp_seq = f_fa.next().strip()
        if( len(tmp_seq) < 5000 ):
            continue
        print ">%s_%d/1\n%s"%(tmp_h,len(tmp_seq),tmp_seq[:1000])
        print ">%s_%d/2\n%s"%(tmp_h,len(tmp_seq),tmp_seq[-1000:])
f_fa.close()
