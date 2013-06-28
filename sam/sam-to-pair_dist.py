#!/usr/bin/env python
import os
import sys

filename_sam = sys.argv[1]

prev_pair_id = ''
pair2hits = dict()

f_sam = open(filename_sam,'r')
f_single = open('%s.single'%filename_sam,'w')
f_single.write('#PairID\tFragID\tTargetID\tTargetCount\tHitTag\n')
f_pair = open('%s.pair'%filename_sam,'w')
f_pair.write('#PairID\tTargetID\tTargetCount\tHitTag(Frag1)\tHittTag(Frag2)\n')
for line in f_sam:
    if( line.startswith('@') ):
        continue
    tokens = line.strip().split("\t")
    
    read_id = tokens[0]
    target_id = tokens[2]
    pair_id = '_'.join(tokens[0].split('_')[:-1])
    start_pos = int(tokens[3])

    frag_dir = read_id[-2:]
    hit_tag = '%s|%s|%d'%(tokens[1],tokens[5],start_pos)

    if( pair_id != prev_pair_id ):
        if( prev_pair_id == '' ):
            pair2hits[pair_id] = dict()
            pair2hits[pair_id][target_id] = {frag_dir:[hit_tag]}
        else:
            tmp_count_t = len(pair2hits[prev_pair_id].keys())

            for tmp_t in sorted(pair2hits[prev_pair_id].keys()):
                if( len(pair2hits[prev_pair_id][tmp_t].keys()) == 1 ):
                    tmp_frag_dir = pair2hits[prev_pair_id][tmp_t].keys()[0]
                    f_single.write('%s\t%s\t%s\t%d\t%s\n'%(prev_pair_id,tmp_frag_dir,tmp_t,tmp_count_t,pair2hits[prev_pair_id][tmp_t][tmp_frag_dir][0]))
                else:
                    frag_list = sorted(pair2hits[prev_pair_id][tmp_t].keys())
                    f_pair.write('%s\t%s\t%d\t%s\t%s\n'%(prev_pair_id,tmp_t,tmp_count_t,';;'.join(pair2hits[prev_pair_id][tmp_t][frag_list[0]]),';;'.join(pair2hits[prev_pair_id][tmp_t][frag_list[1]])))

            pair2hits = dict()
            pair2hits[pair_id] = dict()
            pair2hits[pair_id][target_id] = {frag_dir:[hit_tag]}
    else:
        if( not pair2hits[pair_id].has_key(target_id) ):
            pair2hits[pair_id][target_id] = dict()
        if( not pair2hits[pair_id][target_id].has_key(frag_dir) ):
            pair2hits[pair_id][target_id][frag_dir] = []
        pair2hits[pair_id][target_id][frag_dir].append(hit_tag)

    prev_pair_id = pair_id
f_sam.close()

for tmp_t in sorted(pair2hits[prev_pair_id].keys()):
    if( len(pair2hits[prev_pair_id][tmp_t].keys()) == 1 ):
        tmp_frag_dir = pair2hits[prev_pair_id][tmp_t].keys()[0]
        f_single.write('%s\t%s\t%s\t%s\n'%(prev_pair_id,tmp_frag_dir,tmp_t,pair2hits[prev_pair_id][tmp_t][tmp_frag_dir][0]))
    else:
        f_pair.write('%s\t%s\t%s\t%s\n'%(prev_pair_id,tmp_t,';;'.join(pair2hits[prev_pair_id][tmp_t]['5']),';;'.join(pair2hits[prev_pair_id][tmp_t]['3'])))

f_single.close()
f_pair.close()
