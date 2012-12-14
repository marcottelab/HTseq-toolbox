#!/usr/bin/python
import os
import sys
import gzip

filename_fa = sys.argv[1]
filename_part = sys.argv[2]

seq_h = ''
seq_list = dict()
seqlen = dict()
f_fa = open(filename_fa,'r')
if( filename_fa.endswith('.gz') ):
    f_fa = gzip.open(filename_fa,'rb')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
        seqlen[seq_h] = 0
    else:
        seq_list[seq_h].append(line.strip())
        seqlen[seq_h] += len(line.strip())
f_fa.close()

q2t = dict()
t2q = dict()
f_part = open(filename_part,'r')
for line in f_part:
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    q_len = int(tokens[1])
    t_id = tokens[2]
    t_len = int(tokens[3])
    if( not q2t.has_key(q_id) ):
        q2t[q_id] = dict()
    q2t[q_id][t_id] = 1
    if( not t2q.has_key(t_id) ):
        t2q[t_id] = dict()
    t2q[t_id][q_id] = 1
f_part.close()

filename_base = filename_fa.split('.')[0]

is_part = dict()
f_out = open('%s.NR_oTx.fa'%filename_base,'w')
for tmp_h in sorted(seqlen.keys(),key=seqlen.get,reverse=True):
    if( is_part.has_key(tmp_h) ):
        continue
    
    if( t2q.has_key(tmp_h) ):
        for tmp_q in t2q[tmp_h].keys():
            is_part[tmp_q] = 1
    
    tmp_seq = ''.join(seq_list[tmp_h])
    f_out.write('>%s\n%s\n'%(tmp_h,tmp_seq))
f_out.close()
