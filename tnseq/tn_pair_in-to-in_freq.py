#!/usr/bin/env python
import os
import sys
import re

filename_tn_pair_in = sys.argv[1]

in_freq = dict()
f_tn_pair = open(filename_tn_pair_in,'r')
for line in f_tn_pair:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    pair_id = tokens[0]
    t_id = tokens[1]
    if( not in_freq.has_key(t_id) ):
        in_freq[t_id] = dict()
    tag1_tokens = tokens[2].split('|')
    tag2_tokens = tokens[3].split('|')

    tag1_pos = int(tag1_tokens[0])
    tag1_strand = tag1_tokens[1]
    tag2_pos = int(tag2_tokens[0])
    
    if( not in_freq[t_id].has_key(tag1_pos) ):
        in_freq[t_id][tag1_pos] = {'+':0, '-':0, 'right':0, 'left':0, 'misc':0}
    in_freq[t_id][tag1_pos][tag1_strand] += 1

    if( tag1_pos < tag2_pos ):
        in_freq[t_id][tag1_pos]['right'] += 1
    elif( tag1_pos > tag2_pos ):
        in_freq[t_id][tag1_pos]['left'] += 1
    else:
        in_freq[t_id][tag1_pos]['misc'] += 1
f_tn_pair.close()

f_out = open('%s.in_freq'%filename_tn_pair_in.replace('.tn_pair_in',''),'w')
f_out.write('#Target\tPos\tLeft\tRight\tMisc\tStrand+\tStrand-\n')
f_out
for tmp_t in sorted(in_freq.keys()):
    for tmp_pos in sorted(in_freq[tmp_t].keys()):
        tmp_freq = in_freq[tmp_t][tmp_pos]
        f_out.write('%s\t%d\t%d\t%d\t%d\t%d\t%d\n'%(tmp_t, tmp_pos, tmp_freq['left'], tmp_freq['right'], tmp_freq['misc'], tmp_freq['+'], tmp_freq['-']))

