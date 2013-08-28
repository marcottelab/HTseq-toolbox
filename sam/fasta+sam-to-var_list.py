#!/usr/bin/env python
import os
import sys

filename_fa = sys.argv[1]
filename_sam = sys.argv[2]

seq_list = dict()
seq_h = ''
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append(line.strip())
f_fa.close()

seq_hit = dict()
for tmp_h in seq_list.keys():
    tmp_seq = ''.join(seq_list[tmp_h]).upper()
    tmp_len = len(tmp_seq)
    seq_hit[tmp_h] = {'ref':tmp_seq, 'ref_len':len(tmp_seq)}
    seq_hit[tmp_h]['A'] = [0 for x in range(0,tmp_len)]
    seq_hit[tmp_h]['T'] = [0 for x in range(0,tmp_len)]
    seq_hit[tmp_h]['G'] = [0 for x in range(0,tmp_len)]
    seq_hit[tmp_h]['C'] = [0 for x in range(0,tmp_len)]
    seq_hit[tmp_h]['N'] = [0 for x in range(0,tmp_len)]

rc = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
def revcomp(tmp_seq):
    rv = []
    for tmp_n in tmp_seq[::-1]:
        rv.append( rc[tmp_n] )
    return ''.join(rv)

f_sam = open(filename_sam,'r')
for line in f_sam:
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    if( len(q_id) == 3 ):
        continue

    strand = 1
    if( int(tokens[1]) & 16 == 16 ):
        strand = -1

    t_id = tokens[2]
    start_pos = int(tokens[3])
    cigar = tokens[5]
    read_seq = tokens[9]
    if( strand < 0 ):
        read_seq = revcomp(read_seq)

    for tmp_read_pos in range(0,len(read_seq)):
        tmp_t_pos = start_pos + tmp_read_pos - 1
        tmp_n_read = read_seq[tmp_read_pos]
        if( tmp_t_pos >= seq_hit[t_id]['ref_len'] ):
            continue
        seq_hit[t_id][tmp_n_read][tmp_t_pos] += 1
f_sam.close()

filename_out = '.'.join(filename_sam.split('.')[:-1])

f_var = open('%s.var_list'%filename_out,'w')
f_gap = open('%s.gap_list'%filename_out,'w')

for tmp_id in seq_hit.keys():
    tmp_ref = seq_hit[tmp_id]['ref']
    tmp_len = len(tmp_ref)

    gap_start = -1
    for tmp_pos in range(0,tmp_len):
        tmp_ref_n = tmp_ref[tmp_pos]
        tmp_count_ref = seq_hit[tmp_id][tmp_ref_n][tmp_pos]
        tmp_count_A = seq_hit[tmp_id]['A'][tmp_pos]
        tmp_count_T = seq_hit[tmp_id]['T'][tmp_pos]
        tmp_count_G = seq_hit[tmp_id]['G'][tmp_pos]
        tmp_count_C = seq_hit[tmp_id]['C'][tmp_pos]
        tmp_count_N = seq_hit[tmp_id]['N'][tmp_pos]
        tmp_count_total = tmp_count_A + tmp_count_T + tmp_count_G + tmp_count_C + tmp_count_N
        
        if( tmp_count_total == 0 ):
            if( gap_start < 0 ):
                gap_start = tmp_pos
            continue

        tmp_max_n = 'N'
        tmp_count_max = 0 
        for tmp_n in ['A','T','G','C']:
            if( seq_hit[tmp_id][tmp_n][tmp_pos] > tmp_count_max ):
                tmp_max_n = tmp_n
                tmp_count_max = seq_hit[tmp_id][tmp_n][tmp_pos]

        if( tmp_count_total > 0 ):
            if( gap_start >= 0 ):
                f_gap.write('%s\tgap\t%d\t%d\n'%(tmp_id,gap_start+1,tmp_pos+1))
                gap_start = -1
            if( tmp_ref_n == tmp_max_n and tmp_count_ref > tmp_count_total * 0.6 ):
                continue

            f_var.write('%s\t%d\t%s\t%s\tA=%d;T=%d;G=%d;C=%d\n'%(tmp_id, tmp_pos+1, tmp_ref_n, tmp_max_n, tmp_count_A, tmp_count_T, tmp_count_G, tmp_count_C))

f_var.close()
f_gap.close()
