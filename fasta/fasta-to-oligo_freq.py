#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]
oligomer_len = int(sys.argv[2])

seq_list = dict()
sys.stderr.write('Read %s ... '%filename_fa)
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        seq_list[tmp_h] = []
    else:
        seq_list[tmp_h].append( line.strip() )
f_fa.close()
sys.stderr.write('Done\n')

sys.stderr.write('Calculate oligomer frequency ...')
oligo_freq = dict()
for tmp_h in seq_list.keys():
    tmp_seq = ''.join(seq_list[tmp_h])
    for i in range(0,len(tmp_seq)-oligomer_len):
        tmp_oligo = tmp_seq[i:i+oligomer_len]
        if( not oligo_freq.has_key(tmp_oligo) ):
            oligo_freq[tmp_oligo] = 0
        oligo_freq[tmp_oligo] += 1
sys.stderr.write('Done\n')

sum_freq = sum(oligo_freq.values())

f_out = open('%s.%d_freq'%(filename_fa,oligomer_len),'w')
for tmp_oligo in sorted(oligo_freq.keys()):
    f_out.write('%s\t%d\t%.4f\n'%(tmp_oligo, oligo_freq[tmp_oligo], oligo_freq[tmp_oligo]*1.0/1000000))
f_out.close()
