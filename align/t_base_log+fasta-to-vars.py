#!/usr/bin/python
import os
import sys
import gzip

filename_base_log = sys.argv[1]
filename_fa = sys.argv[2]
filename_vars = filename_base_log.replace('.t_base_log','')+'.vars'

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


t_id = 'NA'
t_seq = ''

f_base_log = open(filename_base_log,'r')
if( filename_base_log.endswith('.gz') ):
    f_base_log = gzip.open(filename_base_log,'rb')
    filename_vars = filename_base_log.replace('.t_base_log.gz','')+'.vars'

f_vars = open(filename_vars,'w')

t_id = ''
t_seq = ''

prev_cov = 0
h_base_log = f_base_log.readline().strip().split("\t")
idx_A = h_base_log.index('A')
idx_T = h_base_log.index('T')
idx_G = h_base_log.index('G')
idx_C = h_base_log.index('C')
f_vars.write('#Start\tEnd\tSize\tStartCov\tEndCov\n')
for line in f_base_log:
    if( line.startswith('Pos') or line.startswith('#') ):
        continue
    
    tokens = line.strip().split("\t")

    if( t_id != tokens[0] ):
        t_id = tokens[0]
        t_seq = ''.join(seq_list[t_id])

    tmp_pos = int(tokens[1])
    tmp_freq = {'A':int(tokens[idx_A]), 'T':int(tokens[idx_T]), 'G':int(tokens[idx_G]), 'C':int(tokens[idx_C])}
    tmp_cov = int(tokens[2]) + int(tokens[3])
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

