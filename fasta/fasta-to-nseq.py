#!/usr/bin/python
import os
import sys
import gzip

filename_fasta = sys.argv[1]

f_fasta = open(filename_fasta,'r')
if( filename_fasta.endswith('.gz') ):
    f_fasta = gzip.open(filename_fasta,'rb')

for line in f_fasta:
    if( not line.startswith('>') ):
        print line.strip()
f_fasta.close()
