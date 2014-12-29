#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_tblog = sys.argv[1]
filename_base = re.sub(r'.t_base_log*','',filename_tblog)

f_tblog = open(filename_tblog,'r')
if( filename_tblog.endswith('.gz') ):
    f_tblog = gzip.open(filename_tblog,'rb')

prev_pos = 0
prev_plus = 0
prev_minus = 0
prev_total = 0
freq_plus = dict()
freq_minus = dict()
freq_total = dict()
for line in f_tblog:
    if( line.startswith('Target') or line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")    
    t_id = tokens[0]
    tmp_pos = int(tokens[1])
    tmp_plus = int(tokens[2])
    tmp_minus = int(tokens[3])
    tmp_total = tmp_plus + tmp_minus

    if( not freq_plus.has_key(t_id) ):
        freq_plus[t_id] = []
        freq_minus[t_id] = []
        freq_total[t_id] = []
        prev_pos = 0
    
    if( prev_plus != tmp_plus ):
        freq_plus[t_id].append("%d\t%d\n"%(tmp_pos,prev_plus))
        freq_plus[t_id].append("%s\t%d\t"%(t_id,tmp_pos))
    if( prev_minus != tmp_minus ):
        freq_minus[t_id].append("%d\t%d\n"%(tmp_pos,prev_minus))
        freq_minus[t_id].append("%s\t%d\t"%(t_id,tmp_pos))
    if( prev_total != tmp_total ):
        freq_total[t_id].append("%d\t%d\n"%(tmp_pos,prev_total))
        freq_total[t_id].append("%s\t%d\t"%(t_id,tmp_pos))

    prev_pos = tmp_pos
    prev_plus = tmp_plus
    prev_minus = tmp_minus
    prev_total = tmp_total
f_tblog.close()

freq_plus[t_id].append("%d\t%d\n"%(tmp_pos,prev_plus))
freq_minus[t_id].append("%d\t%d\n"%(tmp_pos,prev_minus))
freq_total[t_id].append("%d\t%d\n"%(tmp_pos,prev_total))

f_plus = open('%s.bg_plus'%filename_base,'w')
for t_id in freq_plus.keys():
    f_plus.write("".join(freq_plus[t_id][1:]))
f_plus.close()

f_minus = open('%s.bg_minus'%filename_base,'w')
for t_id in freq_minus.keys():
    f_minus.write("".join(freq_minus[t_id][1:]))
f_minus.close()

f_total = open('%s.bg_total'%filename_base,'w')
for t_id in freq_total.keys():
    f_total.write("".join(freq_total[t_id][1:]))
f_total.close()
