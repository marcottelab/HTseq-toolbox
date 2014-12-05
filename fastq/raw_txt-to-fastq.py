#!/usr/bin/env python
import os
import sys
import gzip

filename_txt = sys.argv[1]

f_txt = gzip.open(filename_txt,'rb')
#f_txt = open(filename_txt,'r')
for line in f_txt:
    tokens = line.strip().split(':')
    header = ':'.join(tokens[:5])
    nseq = tokens[5]
    qseq = ':'.join(tokens[6:])
    print "@%s\n%s\n+\n%s"%(header,nseq,qseq)
f_txt.close()
