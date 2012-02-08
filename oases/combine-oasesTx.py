#!/usr/bin/python
import os
import sys
import gzip

prefix = sys.argv[1]
len_cutoff = 400

filename_out = '%s.oasesTx.fa'%(prefix)
filename_short = '%s.oasesTx.short%s_fa'%(prefix,len_cutoff)

seq_list = dict()
for filename in os.listdir('.'):
    if( not filename.startswith(prefix) ):
        continue
    if( filename == filename_out or filename == filename_short):
        continue

    sample_name = filename.replace('.oasesTx.fa','')
    sys.stderr.write('Read %s (%s)\n'%(filename,sample_name))
    f = open(filename,'r')
    if( filename.endswith('.gz') ):
        sample_name = sample_name.replace('.gz','')
        f = gzip.open(filename,'rb')
    for line in f:
        if( line.startswith('>') ):
            h = line.strip().replace('_Transcript','').replace('Locus',sample_name)
            seq_list[h] = []
        else:
            seq_list[h].append( line.strip() )
    f.close()

count_short = 0
count_total = 0
f_out = open('%s.oasesTx.fa'%(prefix),'w')
f_short = open('%s.oasesTx_short%s.fa'%(prefix,len_cutoff),'w')
for tmp_h in seq_list.keys():
    count_total += 1
    tmp_seq = ''.join(seq_list[tmp_h])
    if( len(tmp_seq) < len_cutoff ):
        f_short.write('%s\n%s\n'%(tmp_h,tmp_seq))
        count_short += 1
    else:
        f_out.write('%s\n%s\n'%(tmp_h,tmp_seq))
f_short.close()
f_out.close()

sys.stderr.write('Total seq=%d, Short seq=%d, Long seq=%d\n'%(count_total,count_short,count_total-count_short))

