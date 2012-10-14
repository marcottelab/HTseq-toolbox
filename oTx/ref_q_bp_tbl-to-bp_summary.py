#!/usr/bin/python
import os
import sys

filename_tbl = sys.argv[1]

q2t = dict()
f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    #q_gene = q_id.split('|')[-1]

    t_id = tokens[1]
    pct_id = float(tokens[2])
    align_len = int(tokens[3])
    q_len = int(tokens[6])
    t_len = int(tokens[9])
    e_value = float(tokens[12])
    bit_score = float(tokens[13])

    ## No more length cutoff, not fair when longest pep is used
    #if( align_len < q_len*0.40 ):
    #    continue

    if( not q2t.has_key(q_id) ):
        q2t[q_id] = dict()
    if( not q2t[q_id].has_key(t_id) ):
        q2t[q_id][t_id] = bit_score
    elif( q2t[q_id][t_id] < bit_score ):
        q2t[q_id][t_id] = bit_score 
f_tbl.close()

f_out = open('%s_summary'%filename_tbl.replace('_tbl',''),'w')
for tmp_q in sorted(q2t.keys()):
    tmp_t_list = sorted(q2t[tmp_q].keys(),key=q2t[tmp_q].get,reverse=True)
    tmp_t_str = ','.join(tmp_t_list)
    if( len(tmp_t_list) > 3 ):
        tmp_t_str = ','.join(tmp_t_list[:3])
        
    f_out.write("%s\t%s\n"%(tmp_q,tmp_t_str))
f_out.close()
