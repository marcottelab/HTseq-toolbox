#!/usr/bin/env python
import os
import sys
import gzip

filename_tbl = sys.argv[1]

best_hit = dict()
f_tbl = open(filename_tbl,'r')
if( filename_tbl.endswith('.gz') ):
    f_tbl = gzip.open(filename_tbl,'rb')

for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    if( len(tokens) < 10 ):
        continue
    q_id = tokens[0]
    t_id = tokens[1]
    pct_id = float(tokens[2])
    align_len = int(tokens[3])
    mismatches = int(tokens[4])
    gap_opens = int(tokens[5])
    q_len = int(tokens[6])
    t_len = int(tokens[9])
    bit_score = float(tokens[-1])
    if( q_id == t_id ):
        continue
    if( not best_hit.has_key(q_id) ):
        best_hit[q_id] = {'t_id':t_id, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'mismatches':mismatches,'gap_opens':gap_opens}
    elif( bit_score > best_hit[q_id]['bit_score'] ):
        best_hit[q_id] = {'t_id':t_id, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'mismatches':mismatches,'gap_opens':gap_opens}
f_tbl.close()

f_best = open('%s_best'%filename_tbl.replace('.gz',''),'w')
f_best.write('#Qid\tQLen\tTid\tTLen\tAlignLen\tMismatches\tGapOpens\tBitScore\n')
for q_id in sorted(best_hit.keys()):
    tmp = best_hit[q_id]
    f_best.write('%s\t%d\t%s\t%d\t%d\t%d\t%d\t%d\n'%(q_id,tmp['q_len'],tmp['t_id'],tmp['t_len'],tmp['align_len'],tmp['mismatches'],tmp['gap_opens'],tmp['bit_score']))
f_best.close()
