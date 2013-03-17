#!/usr/bin/python
import os
import sys

data_name = sys.argv[1]

frames = dict()
for filename in os.listdir('.'):
    if( not filename.startswith(data_name) ):
        continue
    if( not filename.endswith('bp+_tbl_best') ):
        continue

    f = open(filename,'r')
    for line in f:
        if( line.startswith('#') ):
            continue
        tokens = line.strip().split("\t")
        q_id = tokens[0]
        q_tokens = q_id.split('|')
        q_frame = q_tokens[-1]
        q_orig_id = '|'.join(q_tokens[:-1])
        align_len = int(tokens[4])

        if( not frames.has_key(q_orig_id) ):
            frames[q_orig_id] = dict()
        if( not frames[q_orig_id].has_key(q_frame) ):
            frames[q_orig_id][q_frame] = {'count':0, 'align_len':align_len}
        frames[q_orig_id][q_frame]['count'] += 1
        if( align_len > frames[q_orig_id][q_frame]['align_len'] ):
            frames[q_orig_id][q_frame]['align_len'] = align_len
    f.close()

count_unique = 0
count_dubious = 0
f_frame = open('%s.unique_frame'%data_name,'w')
f_dubious = open('%s.dubious_frame'%data_name,'w')
for tmp_q in sorted(frames.keys()):
    if( len(frames[tmp_q].keys()) == 1 ):
        f_frame.write("%s|%s\n"%(tmp_q,frames[tmp_q].keys()[0]))
        count_unique += 1
    else:
        out_map = dict()
        tmp_longest_frame = ''
        tmp_longest_len = 0
        for tmp_frame in frames[tmp_q].keys():
            tmp = frames[tmp_q][tmp_frame]
            if( tmp['align_len'] > tmp_longest_len ):
                tmp_longest_len = tmp['align_len']
                tmp_longest_frame = tmp_frame
            out_map[ '%s=%d|%d'%(tmp_frame,tmp['count'],tmp['align_len']) ] = tmp['count']
        
        f_dubious.write("%s\t%s\n"%(tmp_q,','.join([x for x in sorted(out_map.keys(),key=out_map.get)] )))
        count_dubious += 1
f_frame.close()
f_dubious.close()

print "unique=%d, dubious=%d"%(count_unique,count_dubious)
