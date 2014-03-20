#!/usr/bin/python
import os
import sys

filename_base_log = sys.argv[1]
filename_fa = sys.argv[2]

seq_list = dict()
seq_h = ''
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip()  )
f_fa.close()

prev_cov = -1
hole_start_cov = 0
hole_end_cov = 0
hole_start = 0
hole_end = 0
hole_cov_list = []

filename_vars = filename_base_log.replace('.base_log','')+'.vars'

t_id = 'NA'
t_seq = ''
f_base_log = open(filename_base_log,'r')
f_vars = open(filename_vars,'w')

prev_cov = 0
h_base_log = f_base_log.readline().strip().split("\t")
idx_A = h_base_log.index('A')
idx_T = h_base_log.index('T')
idx_G = h_base_log.index('G')
idx_C = h_base_log.index('C')
f_vars.write('#Start\tEnd\tSize\tStartCov\tEndCov\n')
for line in f_base_log:
    if( line.startswith('Pos') ):
        continue
    if( line.startswith('#Target:') ):
        t_id = line.replace('#Target:','').strip()
        if( not seq_list.has_key(t_id) ):
            sys.stderr.write('No seq: %s\n'%t_id)
            sys.exit(1)
        t_seq = ''.join(seq_list[t_id])
        continue

    tokens = line.strip().split("\t")
    tmp_pos = int(tokens[0])
    tmp_freq = {'A':int(tokens[idx_A]), 'T':int(tokens[idx_T]), 'G':int(tokens[idx_G]), 'C':int(tokens[idx_C])}
    tmp_cov = int(tokens[1]) + int(tokens[2])
    if( tmp_cov == 0 ):
        continue

    tmp_n_list = sorted(tmp_freq.keys(), key=tmp_freq.get)
    top_n = tmp_n_list[-1]
    if( tmp_freq[top_n] > tmp_cov * 0.75 ):
        if( top_n != t_seq[tmp_pos] ):
            f_vars.write('MUT\t%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\n'%(tmp_pos,t_seq[tmp_pos],top_n,tmp_cov,prev_cov,tmp_freq['A'],tmp_freq['T'],tmp_freq['G'],tmp_freq['C']))
    elif( top_n != t_seq[tmp_pos] ):
        f_vars.write('HET\t%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\n'%(tmp_pos,t_seq[tmp_pos],top_n,tmp_cov,prev_cov,tmp_freq['A'],tmp_freq['T'],tmp_freq['G'],tmp_freq['C']))
    else:
        f_vars.write('het\t%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\n'%(tmp_pos,t_seq[tmp_pos],top_n,tmp_cov,prev_cov,tmp_freq['A'],tmp_freq['T'],tmp_freq['G'],tmp_freq['C']))
    prev_cov = tmp_cov
f_base_log.close()
f_vars.close()

