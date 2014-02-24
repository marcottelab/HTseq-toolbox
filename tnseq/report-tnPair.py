#!/usr/bin/env python
import os
import sys
import re

filename_tnPair = sys.argv[1]

fragment_len = 20
boundary_len = 10

p_hit = re.compile(r'[ATGC]{10,}')

def get_idx_and_seq(tmp_seq):
    tmp_count = 0
    for tmp_m in p_hit.finditer(tmp_seq):
        tmp_count += 1
    if( tmp_count > 1 ):
        return -1,'NA'

    seq_len = len(tmp_seq)
    tmp_start = tmp_m.start()
    tmp_end = tmp_m.end()
    if( tmp_start > boundary_len ):
        tmp_fragment_start = max(tmp_start-fragment_len, 0)
        tmp_fragment_end = min(tmp_start+fragment_len,seq_len)
        tmp_seq = '%s.%s'%(tmp_seq[tmp_fragment_start:tmp_start], tmp_seq[tmp_start:tmp_fragment_end])
        return 0,tmp_seq

    if( len(tmp_seq) - tmp_end > boundary_len ):
        tmp_fragment_start = max(tmp_end-fragment_len, 0)
        tmp_fragment_end = min(tmp_end+fragment_len,seq_len)
        tmp_seq = '%s.%s'%(tmp_seq[tmp_fragment_start:tmp_end], tmp_seq[tmp_end:tmp_fragment_end])
        return 1,tmp_seq
    
    return -1, 'NA'

f_tnPair = open(filename_tnPair,'r')
f_out = open('%s.txt'%filename_tnPair,'w')
for line in f_tnPair:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    pair_id = tokens[0]
    r1_tokens = tokens[1].split('|')
    r2_tokens = tokens[2].split('|')

    r1_pos_idx, r1_seq = get_idx_and_seq(tokens[3])
    r2_pos_idx, r2_seq = get_idx_and_seq(tokens[4])

    if( r1_pos_idx >= 0 and r2_pos_idx >=  0 ):
        f_out.write("%s\t%s\t%s\t%s\t%s\n"%(pair_id, r1_tokens[r1_pos_idx], r1_seq, r2_tokens[r2_pos_idx], r2_seq))
    elif( r1_pos_idx >= 0 ):
        f_out.write("%s\t%s\t%s\t%s\t%s\n"%(pair_id, r1_tokens[r1_pos_idx], r1_seq, r2_tokens[0], tokens[4][:fragment_len]))
    elif( r2_pos_idx >= 0 ):
        f_out.write("%s\t%s\t%s\t%s\t%s\n"%(pair_id, r1_tokens[0], tokens[3][:fragment_len], r2_tokens[r2_pos_idx], r2_seq))
f_tnPair.close()
f_out.close()
