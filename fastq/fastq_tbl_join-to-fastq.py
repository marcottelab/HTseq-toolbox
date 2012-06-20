#!/usr/bin/env python
import os
import sys

filename_tbl = sys.argv[1]

f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split()
    id = tokens[0]
    nseq1 = tokens[1]
    qseq1 = tokens[2]
    nseq2 = tokens[6]
    qseq2 = tokens[7]
    print "%s/1\n%s\n+\n%s"%(id,nseq1,qseq1)
    print "%s/2\n%s\n+\n%s"%(id,nseq2,qseq2)
f_tbl.close()
