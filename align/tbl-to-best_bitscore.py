#!/usr/bin/env python
import os
import sys
import gzip

filename_tbl = sys.argv[1]
filename_out = '%s_best'%filename_tbl.replace('.gz','')

best_hit = dict()
f_tbl = open(filename_tbl,'r')
if( filename_tbl.endswith('.gz') ):
    filename_out = '%s_best'%filename_tbl.replace('.gz','')
    f_tbl = gzip.open(filename_tbl,'rb')

for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    if( len(tokens) < 10 or line.find('#') > 1 ):
        continue
    q_id = tokens[0]
    t_id = tokens[1]
    pct_id = float(tokens[2])
    align_len = int(tokens[3])
    mismatches = int(tokens[4])
    gap_opens = int(tokens[5])
    q_len = int(tokens[6])
    t_len = int(tokens[9])
    evalue = float(tokens[-2])
    bit_score = float(tokens[-1])
    if( q_id == t_id ):
        continue
    if( not best_hit.has_key(q_id) ):
        best_hit[q_id] = {'t_id':t_id, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'mismatches':mismatches,'gap_opens':gap_opens, 'evalue':evalue}
    elif( bit_score > best_hit[q_id]['bit_score'] ):
        best_hit[q_id] = {'t_id':t_id, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'mismatches':mismatches,'gap_opens':gap_opens, 'evalue':evalue}
f_tbl.close()

f_best = open(filename_out,'w')
f_best.write('#Qid\tQLen\tTid\tTLen\tAlignLen\tMismatches\tGapOpens\tBitScore\tEvalue\n')
for q_id in sorted(best_hit.keys()):
    tmp = best_hit[q_id]
    f_best.write('%s\t%d\t%s\t%d\t%d\t%d\t%d\t%.1f\t%.2e\n'%(q_id,tmp['q_len'],tmp['t_id'],tmp['t_len'],tmp['align_len'],tmp['mismatches'],tmp['gap_opens'],tmp['bit_score'],tmp['evalue']))
f_best.close()
