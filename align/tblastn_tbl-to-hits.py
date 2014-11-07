#!/usr/bin/env python
import os
import sys
import gzip
import re

filename_tbl = sys.argv[1]
filename_base = re.sub(r'_tbl$','',filename_tbl)

f_tbl = open(filename_tbl,'r')
if( filename_tbl.endswith('.gz') ):
    f_tbl = gzip.open(filename_tbl,'rb')
    filename_base = re.sub(r'_tbl.gz$','',filename_tbl)

max_span = 1000000
min_ratio = 0.5
if( len(sys.argv) > 2 ):
    min_ratio = float(sys.argv[2])

## don't consider BLAST hit if align_ratio is less than this.
min_align_hit_ratio = 50

q2hits = dict()
q_len = dict()
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_tokens = tokens[0].split('|')
    q_id = '%s|%s'%(q_tokens[0].lower(),q_tokens[3])
    t_id = tokens[1]
    align_ratio = float(tokens[2])
    if( align_ratio < min_align_hit_ratio ):
        continue

    align_len = int(tokens[3])
    tmp_qlen = int(tokens[6])
    q_start = int(tokens[7])
    q_end = int(tokens[8])
    t_start = int(tokens[10])
    t_end = int(tokens[11])
    tmp_strand = '+'
    if( t_end < t_start ):
        tmp_strand = '-'

    tmp_align_len = q_end - q_start
    if( not q2hits.has_key(q_id) ):
        q2hits[q_id] = dict()
        q_len[q_id] = tmp_qlen
    if( not q2hits[q_id].has_key(t_id) ):
        q2hits[q_id][t_id] = dict()

    if( not q2hits[q_id][t_id].has_key(t_start) ):
        q2hits[q_id][t_id][t_start] = {'strand':tmp_strand, 'q_start':q_start, 'q_end':q_end, 'align_len':tmp_align_len}
    
    ## If there is another hit starting with same t_start, take a hit with longest align_len
    elif( q2hits[q_id][t_id][t_start]['align_len'] < tmp_align_len  ):
        q2hits[q_id][t_id][t_start] = {'strand':tmp_strand, 'q_start':q_start, 'q_end':q_end, 'align_len':tmp_align_len}
f_tbl.close()

f_out = open('%s_hits%02d'%(filename_base,min_ratio*100),'w')
f_out.write("#Q_id\tT_id\tStrand\tT_start\tT_end\tAlignRatio\tAlignLen\n")
for q_id in q2hits.keys():
    for t_id in q2hits[q_id].keys():
        t_start_list = sorted(q2hits[q_id][t_id].keys())

        prev_start = 0
        prev_end = 0
        prev_t_start = 0
        prev_align_len = 0
        init_t_start = 0
        concat_len = 0
        for t_start in sorted(t_start_list):
            tmp_hit = q2hits[q_id][t_id][t_start]
            tmp_align_len = tmp_hit['align_len']
            tmp_ratio = tmp_align_len*1.0/q_len[q_id] 

            if( tmp_ratio > min_ratio ):
                ## Query is covered by single hit (maybe single exon gene?)
                f_out.write("%s\t%s\t%s\t%d\t%d\t%.3f\t%d\n"%(q_id,t_id,tmp_hit['strand'],t_start,t_start+tmp_align_len,tmp_ratio,tmp_align_len))
                concat_len = 0
                init_t_start = 0
                prev_t_start = 0
                prev_start = 0
                prev_end = 0
                prev_align_len = 0
                continue

            if( prev_start == 0 and prev_end == 0 ):
                ## First hit, but not sufficiently covers query. First fragment of whole hit
                init_t_start = t_start
                prev_t_start = t_start
                prev_start = tmp_hit['q_start']
                prev_end = tmp_hit['q_end']
                prev_align_len = (tmp_hit['q_end'] - tmp_hit['q_start'])
                concat_len = prev_align_len
                continue

            elif( t_start - prev_t_start > max_span ):
                ## Too far away from previous hit, so judge previous hit and move on.
                tmp_ratio = concat_len*1.0/q_len[q_id]
                if( tmp_ratio > min_ratio ):
                    f_out.write("%s\t%s\t%s\t%d\t%d\t%.3f\t%d\n"%(q_id,t_id,tmp_hit['strand'],init_t_start,prev_t_start+prev_align_len,tmp_ratio,concat_len))

                init_t_start = t_start
                prev_t_start = t_start
                prev_start = tmp_hit['q_start']
                prev_end = tmp_hit['q_end']
                prev_align_len = (tmp_hit['q_end'] - tmp_hit['q_start'])
                concat_len = prev_align_len
        
            elif( tmp_hit['strand'] == '+' and prev_end < tmp_hit['q_end'] ):
                ## Hit continues
                prev_start = tmp_hit['q_start']
                prev_end = tmp_hit['q_end']
                prev_t_start = t_start
                prev_align_len = (tmp_hit['q_end'] - tmp_hit['q_start'])
                concat_len += prev_align_len

            elif( tmp_hit['strand'] == '-' and prev_start > tmp_hit['q_start'] ):
                ## Hit continues
                prev_start = tmp_hit['q_start']
                prev_end = tmp_hit['q_end']
                prev_t_start = t_start
                prev_align_len = (tmp_hit['q_end'] - tmp_hit['q_start'])
                concat_len += prev_align_len

            else:      
                ## Hit discontinues, so judge previos hit and move on.
                tmp_ratio = concat_len*1.0/q_len[q_id]
                if( tmp_ratio > min_ratio ):
                    f_out.write("%s\t%s\t%s\t%d\t%d\t%.3f\t%d\n"%(q_id,t_id,tmp_hit['strand'],init_t_start,prev_t_start+prev_align_len,tmp_ratio,concat_len))

                init_t_start = t_start
                prev_t_Start = t_start
                prev_start = tmp_hit['q_start']
                prev_end = tmp_hit['q_end']
                prev_align_len = (tmp_hit['q_end'] - tmp_hit['q_start'])
                concat_len = prev_align_len
        
        ## Judge the last hit.
        tmp_ratio = concat_len*1.0/q_len[q_id]
        if( tmp_ratio > min_ratio ):
            f_out.write("%s\t%s\t%s\t%d\t%d\t%.3f\t%d\n"%(q_id,t_id,tmp_hit['strand'],init_t_start,prev_t_start+prev_align_len,tmp_ratio,concat_len))
f_out.close()
