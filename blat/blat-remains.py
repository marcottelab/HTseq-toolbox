#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]
filename_psl = sys.argv[2]

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
f_psl = open(filename_psl,'r')
for line in f_psl:
    tokens = line.strip().split("\t")
    if( len(tokens) < 10 or len(tokens) < 18 ):
        continue
    q_id = tokens[9]
    q_list.append(q_id)
f_psl.close()

last_q_id = q_list[-1]
remain_q_list = list( set(seq_list.keys()) - set(q_list) )
remain_q_list.append(last_q_id)

f_out = open('%s.remains'%filename_fa,'w')
for tmp_q in remain_q_list:
    f_out.write('%s\n%s\n'%(tmp_q,''.join(seq_list[tmp_q])))
f_out.close()
    
