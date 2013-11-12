#!/usr/bin/env python
import os
import sys
import gzip

filename_tbl = sys.argv[1]
filename_base = filename_tbl

min_align_len = 12

f_tbl = open(filename_tbl,'r')
if( filename_tbl.endswith('.gz') ):
    filename_base = filename_base.rstrip('.gz','')
    f_tbl = gzip.open(filename_tbl,'rb')

hits = dict()
q_align = dict()
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
    q_start = int(tokens[7])
    q_end = int(tokens[8])
    t_len = int(tokens[9])
    evalue = float(tokens[-2])
    bit_score = float(tokens[-1])

    if( q_id == t_id ):
        continue
    
    if( align_len < min_align_len ):
        continue
    
    if( not hits.has_key(q_id) ):
        hits[q_id] = dict()
        q_align[q_id] = [0 for x in range(0,q_len)]

    if( not hits[q_id].has_key(t_id) ):
        hits[q_id][t_id] = {'q_start':q_start, 'q_end':q_end, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'mismatches':mismatches,'gap_opens':gap_opens, 'evalue':evalue}

    elif( bit_score > hits[q_id][t_id]['bit_score'] ):
        hits[q_id][t_id] = {'q_start':q_start, 'q_end':q_end, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 'mismatches':mismatches,'gap_opens':gap_opens, 'evalue':evalue}
f_tbl.close()

f_fusion= open('%s_fusion'%filename_base,'w')
f_fusion.write('#Qid\tQLen\tQrange\tTid\tTLen\tAlignLen\tMismatches\tGapOpens\tBitScore\tEvalue\n')
for q_id in sorted(hits.keys()):
    t_bit_score = dict()
    for t_id in hits[q_id].keys():
        t_bit_score[t_id] = hits[q_id][t_id]['bit_score']
    
    out_str = []
    for t_id in sorted(t_bit_score.keys(),key=t_bit_score.get, reverse=True):
        tmp = hits[q_id][t_id]

        count_new_cov = 0
        count_overlap = 0
        for i in range(tmp['q_start']-1,tmp['q_start']+tmp['align_len']-1):
            if( i >= tmp['q_len'] ):
                continue

            if( q_align[q_id][i] == 0 ):
                count_new_cov += 1
            else:
                count_overlap += 1

        if( count_new_cov < min_align_len or count_overlap > min_align_len ):
            continue

        out_str.append('%s\t%d\t%d-%d\t%s\t%d\t%d\t%d\t%d\t%.1f\t%.2e\n'%(q_id,tmp['q_len'],tmp['q_start'],tmp['q_start']+tmp['align_len'],t_id,tmp['t_len'],tmp['align_len'],tmp['mismatches'],tmp['gap_opens'],tmp['bit_score'],tmp['evalue']))

        for i in range(tmp['q_start']-1,tmp['q_start']+tmp['align_len']-1):
            if( i >= tmp['q_len'] ):
                continue
            q_align[q_id][i] = 1

    if( len(out_str) <= 1 ):
        continue

    for tmp in out_str:
        f_fusion.write('%s'%tmp)
f_fusion.close()
