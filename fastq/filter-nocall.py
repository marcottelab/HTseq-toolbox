#!/usr/bin/python
import os
import sys
import gzip

filename_fastq = sys.argv[1]

count_total = 0
count_nocall = 0
count_low_complex = 0

filename_base = filename_fastq.replace('.fastq','')
if( filename_base.find('.called.') >= 0 ):
    sys.stderr.write("%s: Already processed. Skip.\n"%filename_fastq)
    sys.exit(1)

f_fastq = open(filename_fastq,'r')
if( filename_fastq.endswith('.gz') ):
    f_fastq = gzip.open(filename_fastq,'rb')
    filename_base = filename_fastq.replace('.fastq.gz','')

f_out = open('%s.called.fastq'%filename_base,'w')
for line in f_fastq:
    if( line.startswith('@') ):
        nseq = f_fastq.next().strip()
        n_set = set( nseq )
        f_fastq.next()
        qseq = f_fastq.next().strip()
        
        count_total += 1
        if('N' in n_set or '.' in n_set ):
            count_nocall += 1
        elif( len(list(n_set)) < 4 ):
            count_low_complex += 1
        else:
            f_out.write("%s\n%s\n+\n%s\n"%(line.strip(),nseq,qseq))
f_fastq.close()
f_out.close()

f_log = open('%s.log'%filename_base,'a')
f_log.write("Command: filter-called.py %s\n"%filename_fastq)
f_log.write("Total reads: %d\n"%count_total)
f_log.write("Total called: %d\n"%(count_total - count_nocall - count_low_complex))
f_log.write("Reads with nocall: %d\n"%count_nocall)
f_log.write("Reads with low complexity (type of N < 4): %d\n"%count_low_complex)
f_log.write("\n")
f_log.close()
