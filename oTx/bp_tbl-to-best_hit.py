#!/usr/bin/env python
import os
import sys

filename_tbl = sys.argv[1]

best_hit = dict()
f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    t_id = tokens[1]
    pct_id = float(tokens[2])
    align_len = int(tokens[3])
    q_len = int(tokens[6])
    t_len = int(tokens[9])
    bit_score = float(tokens[-1])
    if( not best_hit.has_key(q_id) ):
        best_hit[q_id] = {'t_id':t_id, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len}
    elif( bit_score > best_hit[q_id]['bit_score'] ):
        best_hit[q_id] = {'t_id':t_id, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len}

f_best = open('%s_best'%filename_tbl,'w')
for q_id in sorted(best_hit.keys()):
    tmp = best_hit[q_id]
    f_best.write('%s\t%d\t%s\t%d\t%d\t%d\n'%(q_id,tmp['q_len'],tmp['t_id'],tmp['t_len'],tmp['align_len'],tmp['bit_score']))
f_best.close()
