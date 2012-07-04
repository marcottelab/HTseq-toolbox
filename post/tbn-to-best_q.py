#!/usr/bin/python
import os
import sys

target2query = dict()
filename_tbl = sys.argv[1]

f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    t_id = tokens[1]
    align_len = int(tokens[3])
    t_start = int(tokens[10])
    t_end = int(tokens[11])
    if( not target2query.has_key(t_id) ):
        target2query[t_id] = {'q_id':q_id,'align_len':align_len,'t_start':t_start,'t_end':t_end}
    elif( target2query[t_id]['align_len'] < align_len ):
        target2query[t_id] = {'q_id':q_id,'align_len':align_len,'t_start':t_start,'t_end':t_end}
f_tbl.close()

for t_id in sorted(target2query.keys()):
    tmp = target2query[t_id]
    print "%s\t%s\t%d\t%d\t%d"%(t_id,tmp['q_id'],tmp['align_len'],tmp['t_start'],tmp['t_end'])
