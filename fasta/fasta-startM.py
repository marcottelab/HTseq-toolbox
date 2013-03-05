#!/usr/bin/env python
import os
import sys

filename_fa = sys.argv[1]

seq_h = ''
seq_list = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip()
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()

for tmp_h in sorted(seq_list.keys()):
    tmp_seq = ''.join(seq_list[tmp_h])
    if( tmp_seq.find('M') < 0 ):
        continue
    tmp_M_pos = tmp_seq.index('M')
    print "%s\n%s"%(tmp_h,tmp_seq[tmp_M_pos:])

