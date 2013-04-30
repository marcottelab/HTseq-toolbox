#!/usr/bin/python
import os
import sys

filename_sum = sys.argv[1]

pair2t = dict()
f_sum = open(filename_sum,'r')
for line in f_sum:
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    pair_id = q_id.replace('.b','x').replace('.g','x')
    
    t1_id = tokens[2]
    t1_align_ratio = float(tokens[4])
    t1_start = int(tokens[7].split(',')[0])

    t2_id = tokens[8]
    a2_align_ratio = 0
    t2_start = -1
    if( t2_id != 'NA' ):
        t2_align_ratio = float(tokens[10])
        t2_start = int(tokens[13].split(',')[0])
    
    if( not pair2t.has_key(pair_id) ):
        pair2t[pair_id] = dict()

    if( not pair2t[pair_id].has_key(t1_id) ):
        pair2t[pair_id][t1_id] = dict()
    
    pair2t[pair_id][t1_id][q_id] = {'align_ratio':t1_align_ratio, 't_start':t1_start}
f_sum.close()

filename_out = filename_sum.replace('.blat_summary','')+'.clone_pair'
f_out = open(filename_out,'w')
f_out.write("PairID\tScaffoldID\tDist\tPos1\tPos2\tAlignRatio\n")
for tmp_pid in sorted(pair2t.keys()):
    #if( len(pair2t[tmp_pid]) != 1 ):
    #    sys.stderr.write('Multi target?: %s - %s\n'%(tmp_pid, ','.join(pair2t[tmp_pid].keys())))
    #    continue
    
    for tmp_tid in pair2t[tmp_pid].keys():
        if( len(pair2t[tmp_pid][tmp_tid]) == 1 ):
            continue
        
        if( len(pair2t[tmp_pid][tmp_tid]) != 2 ):
            sys.stderr.write("What is this?: %s - %s\n"%(tmp_pid,tmp_tid))
            sys.exit(1)
        
        q_list = pair2t[tmp_pid][tmp_tid].keys()
        tmp1 = pair2t[tmp_pid][tmp_tid][q_list[0]]
        tmp2 = pair2t[tmp_pid][tmp_tid][q_list[1]]
        
        f_out.write("%s\t%s\t%d\t%d\t%d\t%.3f;%.3f\n"%(tmp_pid,tmp_tid,tmp1['t_start'],tmp2['t_start'],abs(tmp1['t_start']-tmp2['t_start']),tmp1['align_ratio'],tmp2['align_ratio']))
f_out.close()
