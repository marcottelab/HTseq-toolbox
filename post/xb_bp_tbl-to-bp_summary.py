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
    t_id = tokens[1]
    pct_id = float(tokens[2])
    align_len = int(tokens[3])
    q_len = int(tokens[6])
    t_len = int(tokens[9])
    e_value = float(tokens[12])
    ## No more length cutoff, not fair when longest pep is used
    #if( align_len < q_len*0.40 ):
    #    continue

    if( not q2t.has_key(q_id) ):
        q2t[q_id] = dict()
    ## Ensembl
    #t_gene = t_id.split('|')[-1]
    ## XenBase
    t_tokens = t_id.split('|')
    t_gene = '%s|%s'%(t_tokens[0],t_tokens[1])
    if( not q2t[q_id].has_key(t_gene) ):
        q2t[q_id][t_gene] = e_value
    elif( q2t[q_id][t_gene] > e_value ):
        q2t[q_id][t_gene] = e_value
f_tbl.close()

f_out = open('%s_summary'%filename_tbl.replace('_tbl',''),'w')
for tmp_q in sorted(q2t.keys()):
    tmp_t_list = sorted(q2t[tmp_q].keys(),key=q2t[tmp_q].get)
    #print tmp_t_list[:3],[q2t[tmp_q][x] for x in tmp_t_list[:3]]
    tmp_t_str = ','.join(tmp_t_list)
    if( len(tmp_t_list) > 3 ):
        tmp_t_str = ','.join(tmp_t_list[:3])
        
    f_out.write("%s\t%s\n"%(tmp_q,tmp_t_str))
f_out.close()
