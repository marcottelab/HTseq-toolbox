#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

h_fa = ''
seqlen = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        h_fa = line.strip().lstrip('>')
        seqlen[h_fa] = 0
    else:
        seqlen[h_fa] += len(line.strip())
f_fa.close()

for h_fa in sorted(seqlen.keys()):
    print "%s\t%d"%(h_fa,seqlen[h_fa])
