#!/usr/bin/python
import os
import sys
import gzip

filename_fastq = sys.argv[1]
f_fastq = open(filename_fastq,'r')
if( filename_fastq.endswith('.gz') ):
    f_fastq = gzip.open(filename_fastq,'rb')

for line in f_fastq:
    if( line.startswith('@') ):
        header = line.strip()
        nseq = f_fastq.next().strip()
        h2 = f_fastq.next().strip()
        qseq = f_fastq.next().strip()
        print nseq
f_fastq.close()
