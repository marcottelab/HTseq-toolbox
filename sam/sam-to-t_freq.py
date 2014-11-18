#!/usr/bin/env python
import os
import sys

filename_sam = sys.argv[1]
filename_out = filename_sam.replace('.sam_hit','')+'.t_freq'

t_map = dict()
f_sam = open(filename_sam,'r')
for line in f_sam:
    if( line.startswith('@') ):
        continue
    tokens = line.strip().split("\t")
    t_id = tokens[2]
    hit_pos = int(tokens[3])
    read_len = int(tokens[5].rstrip('M'))
    MD = tokens[12].replace('MD:Z:','')
    tmp_min = int(hit_pos)
    tmp_max = tmp_min + read_len

    if( not t_map.has_key(t_id) ):
        t_map[t_id] = {'count':0,'perfect_count':0,'min_pos':-1,'max_pos':-1,'perfect_min_pos':-1,'perfect_max_pos':-1}

    t_map[t_id]['count'] += 1
    if( t_map[t_id]['min_pos'] == -1 or t_map[t_id]['min_pos'] > tmp_min ):
        t_map[t_id]['min_pos'] = tmp_min
    if( t_map[t_id]['max_pos'] == -1 or t_map[t_id]['max_pos'] < tmp_max ):
        t_map[t_id]['max_pos'] = tmp_max

    if( MD.find('A')<0 and MD.find('T')<0 and MD.find('G')<0 and MD.find('C')<0 ):
        t_map[t_id]['perfect_count'] += 1
        if( t_map[t_id]['perfect_min_pos'] == -1 or t_map[t_id]['perfect_min_pos'] > tmp_min ):
            t_map[t_id]['perfect_min_pos'] = tmp_min
        if( t_map[t_id]['perfect_max_pos'] == -1 or t_map[t_id]['perfect_max_pos'] < tmp_max ):
            t_map[t_id]['perfect_max_pos'] = tmp_max
f_sam.close()

f_out = open(filename_out,'w')
f_out.write('#TargetID\tCount\tMinPos\tMaxPos\tPerfectCount\tPerfectMinPos\tPerfectMaxPos\n')
for t_id in sorted(t_map.keys()):
    tmp_map = t_map[t_id]
    f_out.write('%s\t%d\t%d\t%d\t%d\t%d\t%d\n'%(t_id,tmp_map['count'],tmp_map['min_pos'],tmp_map['max_pos'],tmp_map['perfect_count'],tmp_map['perfect_min_pos'],tmp_map['perfect_max_pos']))
f_out.close()
