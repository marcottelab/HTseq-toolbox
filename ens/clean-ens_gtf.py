#!/usr/bin/python
import os
import sys

filename_gtf = sys.argv[1]
f_gtf = open(filename_gtf,'r')
for line in f_gtf:
    tokens = line.strip().split("\t")
    if( len(tokens[0]) > 2 ):
        continue
    print line.strip()
f_gtf.close()
