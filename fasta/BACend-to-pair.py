#!/usr/bin/env python
import os
import sys
import re

filename_fa = sys.argv[1]
filename_out = re.sub(r'.fa[sta.gz]*$','',filename_fa)

min_len = 500

seq_list = dict()
seq_h = ''

f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().split()[0].lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()

pair_seq = dict()
for tmp_h in sorted(seq_list.keys()):
    tmp_seq = ''.join(seq_list[tmp_h])
    long_seq = ''
    for tmp_long_seq in tmp_seq.split('X'):
        if( len(tmp_long_seq) > len(long_seq) ):
            long_seq = tmp_long_seq
    if( len(long_seq) < min_len ):
        continue
    
    pair_id = tmp_h.split('.')[0]
    if( not pair_seq.has_key(pair_id) ):
        pair_seq[pair_id] = dict()
    pair_seq[pair_id][tmp_h] = long_seq

f_pair = open('%s_pair.fa'%filename_out,'w')
f_single = open('%s_single.fa'%filename_out,'w')
for tmp_p in sorted(pair_seq.keys()):
    if( len(pair_seq[tmp_p].keys()) == 2 ):
        for tmp_h in sorted(pair_seq[tmp_p].keys()):
            f_pair.write('>%s\n%s\n'%(tmp_h,pair_seq[tmp_p][tmp_h]))
    else:
        for tmp_h in sorted(pair_seq[tmp_p].keys()):
            f_single.write('>%s\n%s\n'%(tmp_h,pair_seq[tmp_p][tmp_h]))
f_pair.close()
f_single.close()
