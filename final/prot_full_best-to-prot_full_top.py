#!/usr/bin/python 
import os
import sys

filename_best = sys.argv[1]
count_top = int(sys.argv[2])

min_t_align_ratio = 0

t2q = dict()
f_best = open(filename_best,'r')
f_best.readline()
for line in f_best:
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    for tmp_t in tokens[1:]:
        if( tmp_t.find('|') < 0 ):
            continue
        tmp_t_tokens = tmp_t.split('|')
        tmp_t_id = '|'.join(tmp_t_tokens[:-2])
        tmp_t_align_ratio = int(tmp_t_tokens[-1])
        if( tmp_t_align_ratio < min_t_align_ratio ):
            continue

        if( not t2q.has_key(tmp_t_id) ):
            t2q[tmp_t_id] = dict()
        t2q[tmp_t_id][q_id] = tmp_t_align_ratio
f_best.close()

q2t = dict()
for tmp_t_id in t2q.keys():
    tmp_q_list = sorted(t2q[tmp_t_id].keys(),key=t2q[tmp_t_id].get,reverse=True)
    for tmp_q in tmp_q_list[:count_top]:
        if( not q2t.has_key(tmp_q) ):
            q2t[tmp_q] = []
        q2t[tmp_q].append(tmp_t_id)

f_out = open('%s.prot_full_top%d'%('.'.join(filename_best.split('.')[:-1]), count_top),'w')
for tmp_q_id in sorted(q2t.keys()):
    f_out.write("%s\t%d\t%s\n"%(tmp_q_id, len(q2t[tmp_q_id]), ';;'.join(q2t[tmp_q_id])))
f_out.close()
