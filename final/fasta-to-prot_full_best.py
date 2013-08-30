#!/usr/bin/env python
import os
import sys

filename_fa = sys.argv[1]
data_name = '.'.join(filename_fa.split('.')[:-1])

q2t = dict()
sp_list = []
for filename_best in os.listdir('.'):
    if( not filename_best.endswith('.bp+_tbl_best') ):
        continue
    if( not filename_best.startswith(data_name) ):
        continue

    sys.stderr.write('Read %s\n'%filename_best)
    sp_name = filename_best.split('.')[-2].split('_')[0]
    sp_list.append(sp_name)

    f_best = open(filename_best,'r')
    for line in f_best:
        if( line.startswith('#') ):
            continue
        tokens = line.strip().split("\t")

        q_id = tokens[0]
        q_len = int(tokens[1])
        t_tokens = tokens[2].split('|')
        t_id = '%s|%s'%(t_tokens[0],t_tokens[3])
        t_len = int(tokens[3])
        align_len = int(tokens[4])

        if( not q2t.has_key(q_id) ):
            q2t[q_id] = dict()
        if( not q2t[q_id].has_key(sp_name) ):
            q2t[q_id][sp_name] = []
        q2t[q_id][sp_name].append( '%s|%d|%d'%(t_id,int(align_len*100.0/q_len),int(align_len*100.0/t_len)) )
    f_best.close()

sp_list = sorted(list(set(sp_list)))

f_out = open('%s.prot_full_best'%data_name,'w')
f_out.write('SeqID\t%s\n'%('\t'.join(sp_list)))

sys.stderr.write('Read %s\n'%filename_fa)
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( not line.startswith('>') ):
        continue

    tmp_h = line.strip().lstrip('>')
    q_id = tmp_h
    if( not q2t.has_key(q_id) ):
        sys.stderr.write('No Query in BLAST:%s\n'%q_id)
        continue
    
    out_str = []
    for tmp_sp in sp_list:
        if( not q2t[q_id].has_key(tmp_sp) ):
            out_str.append('NA')
        else:
            out_str.append( ','.join( sorted(list(set(q2t[q_id][tmp_sp]))) ) )
    
    f_out.write('%s\t%s\n'%(q_id,'\t'.join(out_str)))
f_fa.close()
f_out.close()
