#!/usr/bin/python
import os
import sys
import gzip

filename_fq = sys.argv[1]

filename_1 = filename_fq.replace('paired','untie_1')
filename_2 = filename_fq.replace('paired','untie_2')

if( filename_fq == filename_1 ):
    sys.exit(1)

f_fq = open(filename_fq,'r')
if( filename_fq.endswith('.gz') ):
    f_fq = gzip.open(filename_fq,'rb')
    filename_1 = filename_1.replace('.gz','')
    filename_2 = filename_2.replace('.gz','')

f_1 = open(filename_1,'w')
f_2 = open(filename_2,'w')

for line in f_fq:
    if( line.startswith('@') ):
        h1 = line.strip()
        nseq1 = f_fq.next().strip()
        qh1 = f_fq.next()
        qseq1 = f_fq.next().strip()
    
        h2 = f_fq.next().strip()
        nseq2 = f_fq.next().strip()
        qh2 = f_fq.next()
        qseq2 = f_fq.next().strip()

        f_1.write('%s\n%s\n+\n%s\n'%(h1,nseq1,qseq1))
        f_2.write('%s\n%s\n+\n%s\n'%(h2,nseq2,qseq2))
f_fq.close()
f_1.close()
f_2.close()

