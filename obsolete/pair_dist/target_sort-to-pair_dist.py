#!/usr/bin/python
import os
import sys

p2r = dict()
filename_tbl = sys.argv[1]
f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    tokens = line.strip().split('\t')
    target_id = tokens[0]
    pair_name = tokens[1]
    read_name = tokens[2]
    hit_strand = tokens[3]
    if( hit_strand != '0' and hit_strand != '16' ):
        continue
    hit_pos = int(tokens[4])
    if( not p2r.has_key(pair_name) ):
        p2r[pair_name] = dict()
    if( not p2r[pair_name].has_key(target_id) ):
        p2r[pair_name][target_id] = {'0':[], '16':[]}
    p2r[pair_name][target_id][hit_strand].append(hit_pos)
f_tbl.close()

filename_base = filename_tbl.replace('.target_sort','')
f_out = open('%s.pair_dist'%filename_base,'w')
for tmp_pname in p2r.keys():
    for tmp_tid in p2r[tmp_pname].keys():
        if( len(p2r[tmp_pname][tmp_tid]['0']) != 1 or len(p2r[tmp_pname][tmp_tid]['16']) != 1 ):
            continue
        tmp_pos0 = p2r[tmp_pname][tmp_tid]['0'][0]
        tmp_pos16 = p2r[tmp_pname][tmp_tid]['16'][0]
        f_out.write('%s\t%s\t%d\t%d\t%d\n'%(tmp_tid,tmp_pname,tmp_pos0,tmp_pos16,tmp_pos16-tmp_pos0))
f_out.close()
