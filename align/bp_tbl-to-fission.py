#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_tbl = sys.argv[1]
filename_base = filename_tbl

min_align_len = 12

f_tbl = open(filename_tbl,'r')
if( filename_tbl.endswith('.gz') ):
    filename_base = re.sub(r'.gz$','',filename_base)
    f_tbl = gzip.open(filename_tbl,'rb')

hits = dict()
t_align = dict()
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
    t_start = int(tokens[10])
    t_end = int(tokens[11])
    evalue = float(tokens[-2])
    bit_score = float(tokens[-1])

    if( q_id == t_id ):
        continue
    
    if( align_len < min_align_len ):
        continue
    
    if( not hits.has_key(t_id) ):
        hits[t_id] = dict()
        t_align[t_id] = [0 for x in range(0,t_len)]

    if( not hits[t_id].has_key(q_id) ):
        hits[t_id][q_id] = {'q_start':q_start, 'q_end':q_end, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 't_start':t_start, 't_end':t_end, 'mismatches':mismatches,'gap_opens':gap_opens, 'evalue':evalue}

    elif( bit_score > hits[t_id][q_id]['bit_score'] ):
        hits[t_id][q_id] = {'q_start':q_start, 'q_end':q_end, 'bit_score':bit_score, 'align_len':align_len, 'q_len':q_len, 't_len':t_len, 't_start':t_start, 't_end':t_end, 'mismatches':mismatches,'gap_opens':gap_opens, 'evalue':evalue}
f_tbl.close()

f_fission= open('%s_fission'%filename_base,'w')
f_fission.write('#Tid\tTLen\tTrange\tQid\tQLen\tAlignLen\tMismatches\tGapOpens\tBitScore\tEvalue\n')
for t_id in sorted(hits.keys()):
    q_bit_score = dict()
    for q_id in hits[t_id].keys():
        q_bit_score[q_id] = hits[t_id][q_id]['bit_score']
    
    out_str = dict()
    for q_id in sorted(q_bit_score.keys(),key=q_bit_score.get, reverse=True):
        tmp = hits[t_id][q_id]

        count_new_cov = 0
        count_overlap = 0
        for i in range(tmp['t_start']-1,tmp['t_start']+tmp['align_len']-1):
            if( i >= tmp['t_len'] ):
                continue

            if( t_align[t_id][i] == 0 ):
                count_new_cov += 1
            else:
                count_overlap += 1

        if( count_new_cov < min_align_len or count_overlap > min_align_len ):
            continue

        out_str[tmp['t_start']] = '%s\t%d\t%d-%d\t%s\t%d\t%d\t%d\t%d\t%.1f\t%.2e\n'%(t_id,tmp['t_len'],tmp['t_start'],tmp['t_start']+tmp['align_len'],q_id,tmp['q_len'],tmp['align_len'],tmp['mismatches'],tmp['gap_opens'],tmp['bit_score'],tmp['evalue'])

        for i in range(tmp['t_start']-1,tmp['t_start']+tmp['align_len']-1):
            if( i >= tmp['t_len'] ):
                continue
            t_align[t_id][i] = 1

    if( len(out_str) <= 1 ):
        continue

    for tmp_t_start in sorted(out_str.keys()):
        f_fission.write('%s'%out_str[tmp_t_start])
f_fission.close()
