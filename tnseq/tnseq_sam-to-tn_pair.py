#!/usr/bin/env python
import os
import sys
import gzip
import re

filename_sam = sys.argv[1]
filename_base = filename_sam.replace('.sam_hit','').replace('.sam','')

len_boundary = 15
min_mismatch = 10

prev_pair_id = ''
pair2hits = dict()

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
    return tmp_start, tmp_end, sum([int(x.rstrip('M')) for x in re_M.findall(tmp_cigar)])

f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')
    filename_base = filename_sam.replace('.sam_hit.gz','').replace('.sam.gz','')

for line in f_sam:
    if( line.startswith('@') and len(line.strip().split()[0]) < 4 ):
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

    pair_id = '/'.join(read_id.split('/')[:-1])
    which_pair = read_id[-2:]
    tmp_startM, tmp_endM, tmp_sumM = get_startM_endM(tmp_cigar)
    tmp_mismatch_len = read_len - tmp_sumM
    
    tmp_boundary = '.'
    ## aSbMcS case
    if( tmp_endM < 0 and tmp_startM < 0 ):
        if( tmp_mismatch_len <= min_mismatch ):
            continue
    ## aMbS case
    elif( tmp_endM < 0 and tmp_mismatch_len > min_mismatch ):
        tmp_b = tmp_startM
        tmp_b_start = tmp_b - len_boundary 
        if( tmp_b_start < 0 ):
            tmp_b_start  = 0
        tmp_b_end = tmp_b + len_boundary
        if( tmp_b_end > read_len ):
            tmp_b_end = read_len
        tmp_boundary = '%s.%s'%(read_seq[tmp_b_start:tmp_b],read_seq[tmp_b:tmp_b_end])
    ## aSbM case
    elif( tmp_startM < 0 and tmp_mismatch_len > min_mismatch ):
        tmp_b = read_len - tmp_endM
        tmp_b_start = tmp_b - len_boundary 
        if( tmp_b_start < 0 ):
            tmp_b_start  = 0
        tmp_b_end = tmp_b + len_boundary
        if( tmp_b_end > read_len ):
            tmp_b_end = read_len
        tmp_boundary = '%s.%s'%(read_seq[tmp_b_start:tmp_b],read_seq[tmp_b:tmp_b_end])

    hit_tag = '%d|%s|%s|%s'%(start_pos, tmp_strand, tmp_cigar, tmp_boundary)

    if( not pair2hits.has_key(pair_id) ):
        pair2hits[pair_id] = dict()
    if( not pair2hits[pair_id].has_key(t_id) ):
        pair2hits[pair_id][t_id] = dict()
    if( not pair2hits[pair_id][t_id].has_key(which_pair) ):
        pair2hits[pair_id][t_id][which_pair] = []
    pair2hits[pair_id][t_id][which_pair].append(hit_tag)
f_sam.close()

f_single = open('%s.tn_single'%filename_base,'w')
f_single.write('#PairID\tTargetID\tWhichPair\tHitTag\n')
f_pair = open('%s.tn_pair'%filename_base,'w')
f_pair.write('#PairID\tTargetID\tHitTag1\tHitTag2\n')
for tmp_p in sorted(pair2hits.keys()):
    for tmp_t in pair2hits[tmp_p].keys():
        which_pair_list = pair2hits[tmp_p][tmp_t].keys()
        if( len(which_pair_list) == 1 ):
            tmp_dir = which_pair_list[0]
            f_single.write('%s\t%s\t%s\t%s\n'%(tmp_p,tmp_t,tmp_dir,';;'.join(pair2hits[tmp_p][tmp_t][tmp_dir])))
        else:
            dir_list = sorted(pair2hits[tmp_p][tmp_t].keys())
            f_pair.write('%s\t%s\t%s\t%s\n'%(tmp_p,tmp_t,';;'.join(pair2hits[tmp_p][tmp_t][dir_list[0]]),';;'.join(pair2hits[tmp_p][tmp_t][dir_list[1]])))

f_single.close()
f_pair.close()
