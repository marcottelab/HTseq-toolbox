#!/usr/bin/env python
import os
import sys

filename_fa = sys.argv[1]
filename_tbl = sys.argv[2]

seq_h = ''
seq_list = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()

q_list = []
f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('# Query:') ):
        q_id = line.strip().split()[-1]
        q_list.append(q_id)
f_tbl.close()

last_q_id = q_list[-1]
remain_q_list = list( set(seq_list.keys()) - set(q_list) )
remain_q_list.append(last_q_id)
if( len(remains_q_list) <= 2 ):
    sys.stderr.write('%s -- Done!\n'%filename_tbl)
else:
    f_out = open('%s.remains'%filename_tbl,'w')
    for tmp_q in remain_q_list:
        f_out.write('>%s\n%s\n'%(tmp_q,''.join(seq_list[tmp_q])))
    f_out.close()
