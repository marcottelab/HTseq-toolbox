#!/usr/bin/env python
import os
import sys
import gzip
import math

filename_tbl = sys.argv[1]

logE_cutoff = int(sys.argv[2])
filename_out = '%s_logE%d'%(filename_tbl.replace('.gz',''), logE_cutoff)

logE_hit = dict()
f_tbl = open(filename_tbl,'r')
if( filename_tbl.endswith('.gz') ):
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
    
    if( math.log10(evalue+1e-100) * -1.0 < logE_cutoff ):
        continue

    tmp_q_ratio = (align_len-mismatches)*100.0/q_len
    tmp_t_ratio = (align_len-mismatches)*100.0/t_len
    if( not logE_hit.has_key(q_id) ):
        logE_hit[q_id] = []
    logE_hit[q_id].append( {'t_id':t_id, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'mismatches':mismatches,'gap_opens':gap_opens, 'evalue':evalue, 'q_ratio':tmp_q_ratio, 't_ratio':tmp_t_ratio} )
f_tbl.close()

f_logE = open(filename_out,'w')
f_logE.write('#Qid\tQLen\tTid\tTLen\tAlignLen\tMismatches\tGapOpens\tBitScore\tEvalue\tQRatio\tTRatio\tHitCount\n')
for q_id in sorted(logE_hit.keys()):
    tmp_count = len(logE_hit[q_id])
    for tmp in logE_hit[q_id]:
        f_logE.write('%s\t%d\t%s\t%d\t%d\t%d\t%d\t%.1f\t%.2e\t%.1f\t%.1f\t%d\n'%(q_id,tmp['q_len'],tmp['t_id'],tmp['t_len'],tmp['align_len'],tmp['mismatches'],tmp['gap_opens'],tmp['bit_score'],tmp['evalue'],tmp['q_ratio'],tmp['t_ratio'],tmp_count))
f_logE.close()
