#!/usr/bin/env python
import os
import sys

usage_mesg = 'Usage: $HST/align/psl-to-top2.py <.psl file>'

if( len(sys.argv) != 2 ):
    sys.stderr.write('%s\n'%usage_mesg)
    sys.exit(1)

filename_psl = sys.argv[1]
filename_out = '%s_top2'%(filename_psl.replace('_psl',''))

q2t = dict()
q2t_ratio = dict()

f_psl = open(filename_psl,'r')
for line in f_psl:
    tokens = line.strip().split("\t")
    if( len(tokens) < 21 or tokens[0] == 'match' ):
        continue
    if( tokens[8] != '+' and tokens[8] != '-' ):
        continue

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

    ## Original match_ratio
    #match_ratio = float(match-mismatch-q_gap_bases)/q_size
    ## Revised match_ratio (Nov. 2013, TK)
    match_ratio = float(match-q_gap_bases)/q_size
    
    if( not q2t.has_key(q_id) ):
        q2t[q_id] = dict()
        q2t_ratio[q_id] = dict()
    if( not q2t[q_id].has_key(t_id) ):
        q2t[q_id][t_id] = dict()
        q2t_ratio[q_id][t_id] = 0
        q2t[q_id][t_id] = {'strand':strand,'q_size':q_size,'t_size':t_size,'block':','.join(block_list),'qstart':','.join(qstart_list),'tstart':','.join(tstart_list), 'q_gap_bases':q_gap_bases,'t_gap_bases':t_gap_bases,'q_gap_count':q_gap_count,'t_gap_count':t_gap_count}
        q2t_ratio[q_id][t_id] = match_ratio
    elif( q2t_ratio[q_id][t_id] < match_ratio ):
        q2t[q_id][t_id] = {'strand':strand,'q_size':q_size,'t_size':t_size,'block':','.join(block_list),'qstart':','.join(qstart_list),'tstart':','.join(tstart_list), 'q_gap_bases':q_gap_bases,'t_gap_bases':t_gap_bases,'q_gap_count':q_gap_count,'t_gap_count':t_gap_count}
        q2t_ratio[q_id][t_id] = match_ratio
    
f_psl.close()

f_out = open(filename_out,'w')
f_out.write('#Qid\tQlen\tT1_id\tT1_strand\tT1_ratio\tT1_block\tQ1_start\tT1_start\tT1_id\tT2_strand\tT2_ratio\tT2_block\tQ2_start\tT2_start\n')
for tmp_q in q2t_ratio.keys():
    t_list = sorted(q2t_ratio[tmp_q].keys(),key=q2t_ratio[tmp_q].get,reverse=True)
    t1 = t_list[0]
    q_size = q2t[tmp_q][t1]['q_size']
    ratio1 = q2t_ratio[tmp_q][t1]
    q_gap_bases1 = q2t[tmp_q][t1]['q_gap_bases']  
    q_gap_count1 = q2t[tmp_q][t1]['q_gap_count']  
    t_gap_bases1 = q2t[tmp_q][t1]['t_gap_bases']  
    t_gap_count1 = q2t[tmp_q][t1]['t_gap_count']  
    strand1 = q2t[tmp_q][t1]['strand']
    block1 = q2t[tmp_q][t1]['block']
    qstart1 = q2t[tmp_q][t1]['qstart']
    tstart1 = q2t[tmp_q][t1]['tstart']

    t2 = 'NA'
    ratio2 = 0
    block2 = 'NA'
    qstart2 = 'NA'
    tstart2 = 'NA'
    strand2 = 'NA'
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
        strand2 = q2t[tmp_q][t2]['strand']
        q_gap_bases2 = q2t[tmp_q][t2]['q_gap_bases']  
        q_gap_count2 = q2t[tmp_q][t2]['q_gap_count']  
        t_gap_bases2 = q2t[tmp_q][t2]['t_gap_bases']  
        t_gap_count2 = q2t[tmp_q][t2]['t_gap_count']  
    
    f_out.write("%s\t%d\t%s\t%s\t%.3f\t%s\t%s\t%s\t"%(tmp_q,q_size,t1,strand1,ratio1,block1,qstart1,tstart1))
    f_out.write("%s\t%s\t%.3f\t%s\t%s\t%s\n"%(t2,strand2,ratio2,block2,qstart2,tstart2))
f_out.close()
