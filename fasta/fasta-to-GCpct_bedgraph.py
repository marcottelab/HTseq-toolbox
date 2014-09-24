#!/usr/bin/env python
import os
import sys
import re

filename_fa = sys.argv[1]
bed_step = 10

if( len(sys.argv) >= 3 ):
    bed_step = int(sys.argv[2])

filename_base = re.sub(r'.(fa|fasta)$','',filename_fa)
f_fa = open(filename_fa,'r')
if( filename_fa.endswith('.gz') ):
    import gzip
    f_fa = gzip.open(filename_fa,'rb')
    filename_base = re.sub(r'.(fa.gz|fasta.gz)$','',filename_fa)
 
seq_h = ''
seq_list = dict()
for line in f_fa:
    if ( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()

f_out = open('%s.GCpct_bedgraph'%filename_base,'w')
for tmp_h in seq_list.keys():
    tmp_seq = ''.join(seq_list[tmp_h])
    for i in range(0,len(tmp_seq)-bed_step,bed_step):
        tmp_fragment = tmp_seq[i:i+bed_step].upper()
        tmp_GCpct = (tmp_fragment.count('G') + tmp_fragment.count('C'))*100.0/bed_step
        f_out.write('%s\t%d\t%d\t%d\n'%(tmp_h,i,i+bed_step,int(tmp_GCpct)))
f_out.close()
