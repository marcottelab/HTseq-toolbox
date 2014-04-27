#!/usr/bin/env python
import os
import sys
import gzip

filename_psl = sys.argv[1]
filename_base = filename_psl.replace('_psl','')

f_psl = open(filename_psl,'r')
if( filename_psl.endswith('_psl.gz') ):
    f_psl = gzip.open(filename_psl,'rb')
    filename_base = filename_psl.replace('_psl.gz','')

q2longest = dict()
for line in f_psl:
    tokens = line.strip().split("\t")
    if( len(tokens) != 21 ):
        continue
    tokens = line.strip().split("\t")
    if( not tokens[0].isdigit() ):
        continue
    align_len = int(tokens[0])
    q_id = tokens[9]
    if( not q2longest.has_key(q_id) ):
        q2longest[q_id] = {'align_len':align_len, 'tokens':tokens}
    elif( q2longest[q_id]['align_len'] < align_len ):
        q2longest[q_id] = {'align_len':align_len, 'tokens':tokens}
f_psl.close()

f_out = open('%s_aln_best'%filename_base,'w')
for q_id in sorted(q2longest.keys()):
    f_out.write('%s\n'%('\t'.join(q2longest[q_id]['tokens'])))
f_out.close()
