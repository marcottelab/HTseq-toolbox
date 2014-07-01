#!/usr/bin/python
import os
import sys
import gzip
import re

filename_fa = sys.argv[1]
len_cutoff = int(sys.argv[2])

filename_base = re.sub(r'.fa[sta.gz]*$','',filename_fa)
len_cutoff_label = '%d'%len_cutoff
if( len_cutoff >= 1000 ):
    len_cutoff_label = '%dk'%(len_cutoff/1000)

seq_h = ''
seq_list = dict()
f_fa = open(filename_fa,'r')
if( filename_fa.endswith('.gz') ):
    f_fa = gzip.open(filename_fa,'rb')

for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()

f_lt = open('%s_lt%s.fa'%(filename_base,len_cutoff_label),'w')
f_set = open('%s_set%s.fa'%(filename_base,len_cutoff_label),'w')

for tmp_h in sorted( seq_list.keys() ):
    tmp_seq = ''.join(seq_list[tmp_h])
    if( len(tmp_seq) > len_cutoff ):
        f_lt.write('>%s\n%s\n'%(tmp_h,tmp_seq))
    else:
        f_set.write('>%s\n%s\n'%(tmp_h,tmp_seq))

f_lt.close()
f_set.close()
