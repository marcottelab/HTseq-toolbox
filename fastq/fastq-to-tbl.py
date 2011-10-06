#!/usr/bin/python
import os
import sys
import gzip

filename_fq = sys.argv[1]

f_fq = open(filename_fq,'r')
if( filename_fq.endswith('gz') ):
    f_fq = gzip.open(filename_fq,'rb')

filename_out = '%s_tbl'%(filename_fq.replace('.gz',''))
f_out = open(filename_out,'w')
sys.stderr.write('Write %s\n'%filename_out)
for h in f_fq:
    if( h.startswith('@') ):
        nseq = f_fq.next()
        qh = f_fq.next()
        qseq = f_fq.next()
        q_list = [ord(x)-64 for x in qseq]
        q_mean = int(float(sum(q_list))/len(q_list))
        q_median = sorted(q_list)[int(len(q_list)*0.5))]
        q_min = min(q_list)
        f_out.write("%s\t%s\t%s\t%d\t%d\t%d\n"%(h,nseq.strip(),qseq.strip()),q_mean,q_median,q_min)
f_fq.close()
f_out.close()
