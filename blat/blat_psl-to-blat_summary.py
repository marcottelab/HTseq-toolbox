#!/usr/bin/python
import os
import sys

filename_tbl = sys.argv[1]

f_tbl = open(filename_tbl,'r')
for i in range(0,5):
    f_tbl.next()

q2t = dict()
q2t_ratio = dict()

for line in f_tbl:
    tokens = line.strip().split("\t")
    match = int(tokens[0])
    mismatch = int(tokens[1])
    q_gap_count = int(tokens[4])
    q_gap_bases = int(tokens[5])
    t_gap_count = int(tokens[6])
    t_gap_bases = int(tokens[7])
    strand = tokens[8]
    q_id = tokens[9]
    q_size = int(tokens[10])
    q_start = int(tokens[11])
    q_end = int(tokens[12])
    t_id = tokens[13]
    t_size = int(tokens[14])
    t_start = int(tokens[15])
    t_end = int(tokens[16])
    block_count = int(tokens[17])
    block_list = [x for x in tokens[18].rstrip(',').split(',')]
    qstart_list  = [x for x in tokens[19].rstrip(',').split(',')]
    tstart_list = [x for x in tokens[20].rstrip(',').split(',')]

    match_ratio = float(match-mismatch-q_gap_bases)/q_size

    #if( q_gap_count > 1 ):
    #    continue

    if( not q2t.has_key(q_id) ):
        q2t[q_id] = dict()
        q2t_ratio[q_id] = dict()
    if(not q2t[q_id].has_key(t_id) ):
        q2t[q_id][t_id] = dict()
        q2t_ratio[q_id][t_id] = 0

    q2t[q_id][t_id] = {'q_size':q_size,'t_size':t_size,'block':','.join(block_list),'qstart':','.join(qstart_list),'tstart':','.join(tstart_list), 'q_gap_bases':q_gap_bases,'t_gap_bases':t_gap_bases,'q_gap_count':q_gap_count,'t_gap_count':t_gap_count}
    q2t_ratio[q_id][t_id] = match_ratio
f_tbl.close()

for tmp_q in q2t_ratio.keys():
    t_list = sorted(q2t_ratio[tmp_q].keys(),key=q2t_ratio[tmp_q].get,reverse=True)
    t1 = t_list[0]
    q_size = q2t[tmp_q][t1]['q_size']
    ratio1 = q2t_ratio[tmp_q][t1]
    q_gap_bases1 = q2t[tmp_q][t1]['q_gap_bases']  
    q_gap_count1 = q2t[tmp_q][t1]['q_gap_count']  
    t_gap_bases1 = q2t[tmp_q][t1]['t_gap_bases']  
    t_gap_count1 = q2t[tmp_q][t1]['t_gap_count']  
    block1 = q2t[tmp_q][t1]['block']
    qstart1 = q2t[tmp_q][t1]['qstart']
    tstart1 = q2t[tmp_q][t1]['tstart']

    t2 = 'NA'
    ratio2 = 0
    block2 = 'NA'
    qstart2 = 'NA'
    tstart2 = 'NA'
    q_gap_bases2 = 0
    q_gap_count2 = 0
    t_gap_bases2 = 0
    t_gap_count2 = 0
    if( len(t_list) > 1 ):
        t2 = t_list[1]
        ratio2 = q2t_ratio[tmp_q][t2]
        block2 = q2t[tmp_q][t2]['block']
        qstart2 = q2t[tmp_q][t2]['qstart']
        tstart2 = q2t[tmp_q][t2]['tstart']
        q_gap_bases2 = q2t[tmp_q][t2]['q_gap_bases']  
        q_gap_count2 = q2t[tmp_q][t2]['q_gap_count']  
        t_gap_bases2 = q2t[tmp_q][t2]['t_gap_bases']  
        t_gap_count2 = q2t[tmp_q][t2]['t_gap_count']  
    
    #print "%s\t%d\t%s\t%.3f\t%s\t%s\t%s\t%s\t%.3f\t%s\t%s\t%s"%(tmp_q,q_size,t1,ratio1,block1,qstart1,tstart1,t2,ratio2,block2,qstart2,tstart2)
    print "%s\t%d\t%s\t%.3f\t%d\t%d\t%s\t%.3f\t%d\t%d"%(tmp_q,q_size,t1,ratio1,q_gap_bases1,q_gap_count1,t2,ratio2,q_gap_bases2,q_gap_count2)
