#!/usr/bin/python
import os
import sys
import math

best_t = dict()
min_diff_t = dict()

filename_tbl = sys.argv[1]
f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    q_lib = q_id.split('_')[0]
    t_id = tokens[1]
    t_lib = t_id.split('_')[0]

    align_len = int(tokens[3])
    mismatches = int(tokens[4])
    gap_opens = int(tokens[5])
    q_len = int(tokens[6])
    t_len = int(tokens[9])
    e_value = float(tokens[12])
    if( gap_opens > 0 ):
        continue
    if( q_lib == t_lib ):
        continue

    if( not best_t.has_key(q_id) ):
        best_t[q_id] = {'t_id':t_id, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'e_value':e_value, 'mismatches':mismatches}
    elif( best_t[q_id]['e_value'] > e_value ):
        best_t[q_id] = {'t_id':t_id, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'e_value':e_value, 'mismatches':mismatches}
f_tbl.close()

filename_out = "%s.another_best"%('.'.join(filename_tbl.split('.')[:-1]))
f_out = open(filename_out,'w')
f_out.write("#Qid\tQLen\tBestTid\tBestTLen\tBestTAlignLen\tBestTMismatches\n")
for q_id in sorted(best_t.keys()):
    tmp_best = best_t[q_id]
    tmp_min_diff = min_diff_t[q_id]

    f_out.write("%s\t%d\t%s\t%d\t%d\t%d\n"%(q_id,tmp_best['q_len'],\
    tmp_best['t_id'],tmp_best['t_len'],tmp_best['align_len'],tmp_best['mismatches']))
f_out.close()
