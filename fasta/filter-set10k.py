#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

h = ''
seqlen = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        h = line.strip()
        seqlen[h] = 0
    else:
        seqlen[h] += len(line.strip())
f_fa.close()

is_print = 0
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        h = line.strip()
        if( seqlen[h] <= 10000 ):
            is_print = 1
            print h
        else:
            is_print = 0
    else:
        if( is_print > 0 ):
            print line.strip()
f_fa.close()

