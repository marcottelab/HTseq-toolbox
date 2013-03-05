#!/usr/bin/python
import os
import sys

filename_tbl = sys.argv[1]
filename_fa = sys.argv[2]

query_list = []
subseq_list = dict()

f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    t_id = tokens[1]
    if( t_id == q_id ):
        query_list.append(q_id)
        continue
    pct_id = float(tokens[2])
    align_len = int(tokens[3])
    mismatches = int(tokens[4])
    gap_opens = int(tokens[5])
    q_len = int(tokens[6])
    t_len = int(tokens[9])
    diff_ratio = float(abs(align_len - q_len))/q_len

    if( diff_ratio > 0.20 ):
        continue

    if( diff_ratio < 0.05 and pct_id > 99 and q_len <= t_len and gap_opens == 0 ):
        if( not subseq_list.has_key(q_id) ):
            subseq_list[q_id] = []
        subseq_list[q_id].append(t_id)
f_tbl.close()

query_list = list(set(query_list))
sys.stderr.write("Total query: %d, Subseq: %d, nr_seq: %d\n"%(len(query_list),len(subseq_list.keys()),len(query_list)-len(subseq_list.keys())))

seq_h = ''
seq_list = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append(line.strip())
f_fa.close()

for tmp_id in list(set(query_list) - set(subseq_list.keys())):
    print ">%s\n%s"%(tmp_id,''.join(seq_list[tmp_id]))
