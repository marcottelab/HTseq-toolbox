#!/usr/bin/env python
import os
import sys
import gzip
import re

filename_sam = sys.argv[1]

#min_mismatch = 20
min_match = 20

## ref: http://sqt.googlecode.com/git-history/hashing/sqt/cigar.py
def get_cigar(tmp_cigar):
    rv = []
    n = ''
    count_M = 0
    for c in tmp_cigar:
        if c.isdigit():
            n += c
        else:
            rv.append( (c, int(n)) )
            if( c == 'M' ):
                count_M += 1
            n = ''
    
    matched_len = 0
    start_pos = 0
    if( count_M > 1 ):
        return start_pos, matched_len
    
    for tag,align_len in rv:
        if( tag == 'M' ):
            matched_len = align_len
            break
        start_pos += align_len
    return start_pos, matched_len

s_counts = dict()
as_counts = dict()
quad_counts = dict()
boundary_counts = dict()

A_counts = dict()
T_counts = dict()
G_counts = dict()
C_counts = dict()

sys.stderr.write('Read %s ... '%filename_sam)
f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')

seq_len = 10000
for line in f_sam:
    if( line.startswith('@') and len(line.strip().split()[0]) < 4 ):
        if( line.startswith('@SQ') ):
            tokens = line.strip().split()
            seq_id = re.sub(r'SN:','',tokens[1])
            seq_len = int(re.sub(r'LN:','',tokens[2]))
            if( not s_counts.has_key(seq_id) ):
                s_counts[seq_id] = [0 for x in range(0,seq_len)]
                as_counts[seq_id] = [0 for x in range(0,seq_len)]
                s_counts[seq_id] = [0 for x in range(0,seq_len)]
                as_counts[seq_id] = [0 for x in range(0,seq_len)]
                quad_counts[seq_id] = [0 for x in range(0,seq_len)]
                boundary_counts[seq_id] = [0 for x in range(0,seq_len)]
                A_counts[seq_id] = [0 for x in range(0,seq_len)]
                T_counts[seq_id] = [0 for x in range(0,seq_len)]
                G_counts[seq_id] = [0 for x in range(0,seq_len)]
                C_counts[seq_id] = [0 for x in range(0,seq_len)]
        continue

    tokens = line.strip().split("\t")
    read_id = tokens[0]
    hit_flag = int(tokens[1])
    t_id = tokens[2]
    start_pos = int(tokens[3])
    read_seq = tokens[9]
    read_len = len(read_seq)
    tmp_cigar = tokens[5]
    tmp_strand = '+'
    if( hit_flag & 16 ):
        tmp_strand = '-'

    tmp_startM, tmp_matched_len = get_cigar(tmp_cigar)
    if( tmp_matched_len < min_match ):
        continue
    
    if( not s_counts.has_key(t_id) and not as_counts.has_key(t_id) ):
        s_counts[t_id] = [0 for x in range(0,seq_len)]
        as_counts[t_id] = [0 for x in range(0,seq_len)]
        s_counts[t_id] = [0 for x in range(0,seq_len)]
        as_counts[t_id] = [0 for x in range(0,seq_len)]
        quad_counts[t_id] = [0 for x in range(0,seq_len)]
        boundary_counts[t_id] = [0 for x in range(0,seq_len)]
        A_counts[t_id] = [0 for x in range(0,seq_len)]
        T_counts[t_id] = [0 for x in range(0,seq_len)]
        G_counts[t_id] = [0 for x in range(0,seq_len)]
        C_counts[t_id] = [0 for x in range(0,seq_len)]

    tmp_start = start_pos - 1
    tmp_end = tmp_start + tmp_matched_len - 1
    tmp_boundary_start = 0
    tmp_boundary_end = 0

    if( tmp_matched_len < read_len ):
        if( tmp_startM > 0 ):
            tmp_boundary_start = tmp_start
        if( tmp_startM + tmp_matched_len < read_len ):
            tmp_boundary_end = tmp_end
    
    tmp_read_count = 1
    #tmp_read_count = int(read_id.split('_')[-1])
    for i in range(tmp_start, tmp_end+1):
        #if( i >= seq_len ):
        #    print i,tmp_start,tmp_end,tokens
        if( tmp_strand == '+' ):
            s_counts[t_id][i] += tmp_read_count
        else:
            as_counts[t_id][i] += tmp_read_count

        tmp_n = read_seq[i-start_pos+tmp_startM+1]
        if( tmp_n == 'A' ):
            A_counts[t_id][i] += tmp_read_count
        elif( tmp_n == 'T' ):
            T_counts[t_id][i] += tmp_read_count
        elif( tmp_n == 'G' ):
            G_counts[t_id][i] += tmp_read_count
        elif( tmp_n == 'C' ):
            C_counts[t_id][i] += tmp_read_count

        if( i < tmp_end-3 ):
            quad_counts[t_id][i] += 1

    if( tmp_boundary_start > 0 ):
        boundary_counts[t_id][tmp_boundary_start-1] += 1
    if( tmp_boundary_end > 0 ):
        boundary_counts[t_id][tmp_boundary_end-1] += 1
f_sam.close()
sys.stderr.write('Done\n')

filename_base = filename_sam.split('.')[0]
filename_log = '%s.base_log'%(filename_base)
f_log = open(filename_log,'w')
f_log.write('Pos\tCount+\tCount-\tQuadruple\tBorder\tA\tT\tG\tC\n')
for t_id in s_counts.keys():
    t_name = t_id.replace('|','_')
    f_log.write('#Target: %s\n'%t_name)
    for i in range(0,len(s_counts[t_id])):
        f_log.write("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n"%(t_id, i, s_counts[t_id][i], as_counts[t_id][i], quad_counts[t_id][i], boundary_counts[t_id][i],A_counts[t_id][i],T_counts[t_id][i],G_counts[t_id][i],C_counts[t_id][i]))
f_log.close()
