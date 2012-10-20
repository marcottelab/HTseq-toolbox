#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        tokens = line.strip().split()
        gene_id = tokens[3].replace('gene:','')
        tx_id = tokens[4].replace('transcript:','')
        print "%s|%s|%s"%(tokens[0],tx_id,gene_id)
    else:
        print line.strip()
f_fa.close()
