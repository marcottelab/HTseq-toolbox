#!/usr/bin/env python
## Assume that the names of pairs are only different the last two characters
## i.e. ABCDE/1--ABCDE/2, ABCDE.b--ABCDE.g
import os
import sys
import gzip
import re

filename_top2 = sys.argv[1]
filename_base = re.sub('_top2$','',filename_top2)

pair2t = dict()
f_top2 = open(filename_top2,'r')
if( filename_top2.endswith('.gz') ):
    f_top2 = gzip.open(filename_top2,'rb')
    filename_base = re.sub('_top2.gz$','',filename_top2)

for line in f_top2:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    pair_id = q_id[:-2]
    q_len = int(tokens[1])
    t_id = tokens[2]
    strand = tokens[3]
    t_ratio = float(tokens[4])
    t_start = int(tokens[7].split(',')[0])

    if( not pair2t.has_key(pair_id) ):
        pair2t[pair_id] = dict()
    if( not pair2t[pair_id].has_key(q_id) ):
        pair2t[pair_id][q_id] = {'q_len':q_len, 't_id':t_id, 'strand':strand, 't_start':t_start}
    elif( pair2t[pair_id][q_id]['q_len'] < q_len ):
        sys.stderr.write('Duplicate query?: %s\n'%q_id)
        pair2t[pair_id][q_id] = {'q_len':q_len, 't_id':t_id, 'strand':strand, 't_start':t_start}
f_top2.close()

same_map = dict()
diff_map = dict()
single_map = dict()

count_same = 0
count_diff = 0
count_same_err = 0
count_err = 0

f_same = open('%s.pair_together'%filename_base,'w')
f_diff = open('%s.pair_apart'%filename_base,'w')
f_err = open('%s.pair_error'%filename_base,'w')

f_same.write('#PairID\tT1id\tQ1pos\tQ2pos\tDist\n')
f_diff.write('#Q1id\tT1id\tT1pos\tT1strand\tQ2id\tT2id\tT2pos\tT2strand\n')
f_err.write('#Q1id\tT1id\tT1pos\tT1strand\tQ2id\tT2id\tT2pos\tT2strand\n')
for tmp_pid in sorted(pair2t.keys()):
    tmp_p = pair2t[tmp_pid]
    qid_list = tmp_p.keys()
    
    if( len(qid_list) == 2 ):
        q1_id = qid_list[0]
        q2_id = qid_list[1]
        tmp_q1 = pair2t[tmp_pid][q1_id]
        tmp_q2 = pair2t[tmp_pid][q2_id]
        
        if( tmp_q1['t_id'] == tmp_q2['t_id'] ):
            if( tmp_q1['strand'] != tmp_q2['strand'] ):
                count_same += 1
                if( tmp_q1['t_start'] > tmp_q2['t_start'] ):
                    tmp = tmp_q1
                    tmp_q1 = tmp_q2
                    tmp_q2 = tmp
                f_same.write('%s\t%s\t%d\t%d\t%d\n'%(tmp_pid,tmp_q1['t_id'],tmp_q1['t_start'],tmp_q2['t_start'],tmp_q2['t_start']-tmp_q1['t_start']))
            else:
                count_same_err += 1
                f_err.write('%s\t%s\t%d\t%s\t%s\t%s\t%d\t%s\n'%(q1_id,tmp_q1['t_id'],tmp_q1['t_start'],tmp_q1['strand'],q2_id,tmp_q2['t_id'],tmp_q2['t_start'],tmp_q2['strand']))
        else:
            count_diff += 1
            f_diff.write('%s\t%s\t%d\t%s\t%s\t%s\t%d\t%s\n'%(q1_id,tmp_q1['t_id'],tmp_q1['t_start'],tmp_q1['strand'],q2_id,tmp_q2['t_id'],tmp_q2['t_start'],tmp_q2['strand']))
    else:
        count_err += len(qid_list)
        #f_err.write('%s\t%s\t%d\t%s\t%s\t%s\t%d\t%s\n'%(q1_id,tmp_q1['t_id'],tmp_q1['t_start'],tmp_q1['strand'],q2_id,tmp_q2['t_id'],tmp_q2['t_start'],tmp_q2['strand']))
f_same.close()
f_diff.close()
f_err.close()

sys.stderr.write('Same: %d, SameErr:%d, Diff: %d, Err: %d\n'%(count_same*2, count_same_err*2, count_diff*2, count_err))
