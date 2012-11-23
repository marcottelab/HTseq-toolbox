#!/usr/bin/python
import os
import sys
import gzip

prefix = sys.argv[1]

filename_out = '%s.combined_oTx.fa'%(prefix)

seq_list = dict()
for filename in os.listdir('.'):
    if( not filename.startswith(prefix) ):
        continue
    if( not filename.endswith('.oTx.fa') ):
        continue
    if( filename == filename_out ):
        continue

    sample_name = filename.replace('.oTx.fa','')
    sys.stderr.write('Read %s (%s)\n'%(filename,sample_name))
    f = open(filename,'r')
    if( filename.endswith('.gz') ):
        sample_name = sample_name.replace('.gz','')
        f = gzip.open(filename,'rb')
    
    seq_h = ''
    for line in f:
        if( line.startswith('>') ):
            seq_h = line.strip().replace('_Transcript','').replace('Locus',sample_name)
            seq_h = seq_h.replace('_Confidence','').replace('_Length','')
            seq_list[seq_h] = []
        else:
            seq_list[seq_h].append( line.strip() )
    f.close()

count_total = 0
multi_seq = dict()
f_out = open(filename_out,'w')
for tmp_h in seq_list.keys():
    count_total += 1
    tmp_seq = ''.join(seq_list[tmp_h])
    if( not multi_seq.has_key(tmp_seq) ):
        multi_seq[tmp_seq] = 0
    multi_seq[tmp_seq] += 1
    f_out.write('%s\n%s\n'%(tmp_h,tmp_seq))
f_out.close()
