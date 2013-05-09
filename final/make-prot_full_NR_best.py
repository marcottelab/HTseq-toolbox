#!/usr/bin/env python
import os
import sys

data_name = sys.argv[1]

frames = dict()
f_frame = open('%s.unique_frame'%data_name,'r')
for line in f_frame:
    frames[ line.strip() ] = 1
f_frame.close()

q2t = dict()
sp_list = []
for filename_best in os.listdir('.'):
    if( not filename_best.endswith('.bp+_tbl_best') ):
        continue
    if( not filename_best.startswith(data_name) ):
        continue

    sys.stderr.write('Read %s\n'%filename_best)
    sp_name = filename_best.split('.')[1].split('_')[0]
    sp_list.append(sp_name)
    f_best = open(filename_best,'r')
    for line in f_best:
        if( line.startswith('#') ):
            continue
        tokens = line.strip().split("\t")
        if( not frames.has_key(tokens[0]) ):
            continue
        #q_id = tokens[0].split('|')[2]
        q_id = '|'.join(tokens[0].split('|')[:-1])
        t_id = tokens[2]
        if( t_id.find('|') >= 0 ):
            t_id = t_id.split('|')[3]
        if( not q2t.has_key(q_id) ):
            q2t[q_id] = dict()
        if( not q2t[q_id].has_key(sp_name) ):
            q2t[q_id][sp_name] = []
        q2t[q_id][sp_name].append(t_id)
    f_best.close()

sp_list = sorted(list(set(sp_list)))

f_out = open('%s.prot_full_NR_best'%data_name,'w')
f_out.write('SeqID\t%s\n'%('\t'.join(sp_list)))
for filename_fa in os.listdir('.'):
    if( not filename_fa.endswith('.prot_full_NR.fa') ):
        continue
    if( not filename_fa.startswith(data_name) ):
        continue
    sys.stderr.write('Read %s\n'%filename_fa)
    #f_fa = open(os.path.join('..','final',filename_fa),'r')
    f_fa = open(filename_fa,'r')
    for line in f_fa:
        if( not line.startswith('>') ):
            continue

        tmp_h = line.strip().lstrip('>')
        #q_id = tmp_h.split('|')[2]
        #q_id = tokens[0]
        q_id = '.'.join(tmp_h.split('.')[1:])
        if( not q2t.has_key(q_id) ):
            sys.stderr.write('No Query in BLAST:%s\n'%q_id)
            continue
        
        out_str = []
        for tmp_sp in sp_list:
            if( not q2t[q_id].has_key(tmp_sp) ):
                out_str.append('NA')
            else:
                out_str.append( ','.join( sorted(list(set(q2t[q_id][tmp_sp]))) ) )
        
        f_out.write('%s.%s\t%s\n'%(tmp_h.split('.')[0],q_id,'\t'.join(out_str)))
    f_fa.close()
f_out.close()
