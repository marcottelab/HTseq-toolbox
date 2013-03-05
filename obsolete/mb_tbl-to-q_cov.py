#!/usr/bin/env python
import os
import sys

filename_tbl = sys.argv[1]

q_cov_best = dict()
f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    t_id  = tokens[1]
    pct_id = float(tokens[2])
    align_len = int(tokens[3])
    mismatches = int(tokens[4])
    gap_opens = int(tokens[5])
    q_len = int(tokens[6])
    t_len = int(tokens[9])
    
    if( pct_id < 95 or gap_opens > 0 ):
        continue
    q_cov = (align_len-mismatches)*100.0/t_len
    if( not q_cov_best.has_key(q_id) ):
        q_cov_best[q_id] = {'q_len':q_len, 't_len':t_len, 't_id':t_id, 'q_cov':q_cov}
    elif( q_cov_best[q_id]['q_cov'] < q_cov ):
        q_cov_best[q_id] = {'q_len':q_len, 't_len':t_len, 't_id':t_id, 'q_cov':q_cov}
f_tbl.close()

for tmp_q in sorted(q_cov_best.keys()):
    tmp = q_cov_best[tmp_q]
    print "%s\t%d\t%s\t%d\t%.3f"%(tmp_q, tmp['q_len'],tmp['t_id'], tmp['t_len'], tmp['q_cov'])
