#!/usr/bin/env python
import os
import sys
import gzip
import re

#filename_sam = sys.argv[1]
#filename_base = re.sub(r'.sam[A-z_.]*$','',filename_sam)
filename_base = sys.argv[1]

min_mismatch = 20

re_M = re.compile('\d+M')
re_endM = re.compile('\d+M$')
re_startM = re.compile('^\d+M')

def get_startM_endM(tmp_cigar):
    tmp_start = re_startM.search(tmp_cigar)
    if( tmp_start == None ):
        tmp_start = -1
    else:
        tmp_start = int(tmp_start.group(0).rstrip('M'))

    tmp_end = re_endM.search(tmp_cigar)
    if( tmp_end == None ):
        tmp_end = -1
    else:
        tmp_end = int(tmp_end.group(0).rstrip('M'))
    
    M_list = re_M.findall(tmp_cigar)
    return tmp_start, tmp_end, sum([int(x.rstrip('M')) for x in M_list]), len(M_list)

s_hits = dict()
as_hits = dict()
s_counts = dict()
as_counts = dict()
double_hits = dict()
boundary_hits = dict()

A_counts = dict()
T_counts = dict()
G_counts = dict()
C_counts = dict()

for filename_sam in os.listdir('.'):
    if( not filename_sam.startswith(filename_base) ):
        continue
    if( filename_sam.find('.sam') < 0 ):
        continue

    sys.stderr.write('Read %s ... '%filename_sam)
    f_sam = open(filename_sam,'r')
    if( filename_sam.endswith('.gz') ):
        f_sam = gzip.open(filename_sam,'rb')
    for line in f_sam:
        if( line.startswith('@') and len(line.strip().split()[0]) < 4 ):
            if( line.startswith('@SQ') ):
                tokens = line.strip().split()
                seq_id = re.sub(r'SN:','',tokens[1])
                seq_len = int(re.sub(r'LN:','',tokens[2]))
                if( not s_hits.has_key(seq_id) ):
                    s_hits[seq_id] = [0 for x in range(0,seq_len)]
                    as_hits[seq_id] = [0 for x in range(0,seq_len)]
                    s_counts[seq_id] = [0 for x in range(0,seq_len)]
                    as_counts[seq_id] = [0 for x in range(0,seq_len)]
                    double_hits[seq_id] = [0 for x in range(0,seq_len)]
                    boundary_hits[seq_id] = [0 for x in range(0,seq_len)]
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

        tmp_startM, tmp_endM, tmp_sumM, tmp_countM = get_startM_endM(tmp_cigar)
        tmp_mismatch_len = read_len - tmp_sumM
        if( tmp_mismatch_len < min_mismatch ):
            continue
        
        tmp_start = 0
        tmp_end = 0
        tmp_boundary_start = 0
        tmp_boundary_end = 0
        ## aM case
        if( tmp_startM > 0 and tmp_startM == tmp_endM ):
            tmp_start = start_pos
            tmp_end = start_pos + tmp_startM - 1
        
        ## aSbMcS case
        if( tmp_endM < 0 and tmp_startM < 0 ):
            if( tmp_countM == 1 ):
                tmp_start = start_pos
                tmp_end = start_pos + tmp_sumM - 1
                tmp_boundary_start = tmp_start
                tmp_boundary_end = tmp_end

        ## aMbS case
        elif( tmp_endM < 0 ):
            tmp_start = start_pos
            tmp_end = start_pos + tmp_startM - 1
            tmp_boundary_end = tmp_end

        ## aSbM case
        elif( tmp_startM < 0 ):
            tmp_start = start_pos
            tmp_end = start_pos + tmp_endM - 1
            tmp_boundary_start = tmp_start

        #tmp_read_count = 1
        tmp_read_count = int(read_id.split('_')[-1])
        if( tmp_start > 0 and tmp_end > 0 ):
            if( tmp_strand == '+' ):
                for i in range(tmp_start-1, tmp_end):
                    s_hits[t_id][i] += 1
                    s_counts[t_id][i] += tmp_read_count

                    tmp_n = read_seq[i-start_pos+1]
                    if( tmp_n == 'A' ):
                        A_counts[t_id][i] += tmp_read_count
                    elif( tmp_n == 'T' ):
                        T_counts[t_id][i] += tmp_read_count
                    elif( tmp_n == 'G' ):
                        G_counts[t_id][i] += tmp_read_count
                    elif( tmp_n == 'C' ):
                        C_counts[t_id][i] += tmp_read_count

                    if( i < tmp_end-1 ):
                        double_hits[t_id][i] += 1
            elif( tmp_strand == '-' ):
                for i in range(tmp_start-1, tmp_end):
                    as_hits[t_id][i] += 1
                    as_counts[t_id][i] += tmp_read_count
                    
                    tmp_n = read_seq[i-start_pos+1]
                    if( tmp_n == 'A' ):
                        A_counts[t_id][i] += tmp_read_count
                    elif( tmp_n == 'T' ):
                        T_counts[t_id][i] += tmp_read_count
                    elif( tmp_n == 'G' ):
                        G_counts[t_id][i] += tmp_read_count
                    elif( tmp_n == 'C' ):
                        C_counts[t_id][i] += tmp_read_count

                    if( i < tmp_end-1 ):
                        double_hits[t_id][i] += 1

        if( tmp_boundary_start > 0 ):
            boundary_hits[t_id][tmp_boundary_start-1] += 1
        if( tmp_boundary_end > 0 ):
            boundary_hits[t_id][tmp_boundary_end-1] += 1
    f_sam.close()
    sys.stderr.write('Done\n')

for t_id in s_hits.keys():
    t_name = t_id.replace('|','_')
    filename_log = '%s.%s.base_log'%(filename_base,t_name)
    f_log = open(filename_log,'w')
    f_log.write('Pos\tCount+\tCount-\tHit+\tHit-\tDouble\tBorder\tA\tT\tG\tC\n')
    for i in range(0,len(s_hits[t_id])):
        f_log.write("%d\t%d\t%d\t%d\t%d\t%d\t%d\n"%(i,s_counts[t_id][i], as_counts[t_id][i], s_hits[t_id][i],as_hits[t_id][i], double_hits[t_id][i], boundary_hits[t_id][i],A_counts[t_id][i],T_counts[t_id][i],G_counts[t_id][i],C_counts[t_id][i]))
    f_log.close()
