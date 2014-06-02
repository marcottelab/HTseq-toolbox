#!/usr/bin/env python
import os
import sys

filename_sam = sys.argv[1]

read2t = dict()
f_sam = open(filename_sam,'r')
for line in f_sam:
    if( line.startswith('@') ):
        continue

    tokens = line.strip().split("\t")
    read_id = tokens[0]
    t_id = tokens[2]
    if( not read2t.has_key(read_id) ):
        read2t[read_id] = []
    read2t[read_id].append(t_id)
f_sam.close()

count_total = len(read2t)
print "total:%d"%count_total
count_unique = 0
count_multi = 0
count_xcross = 0

def get_pair_name(tmp):
    return tmp.split('|')[0].replace('-a','').replace('-b','')

for tmp_r_id in read2t.keys():
    if( len(read2t[tmp_r_id]) == 1 ):
        count_unique += 1
    else:
        if( len(read2t[tmp_r_id]) == 2 and get_pair_name(read2t[tmp_r_id][0]) == get_pair_name(read2t[tmp_r_id][1]) ):
            count_xcross += 1
        else:
            count_multi += 1

print "unique: %d (%.2f pct), multi: %d, xross: %d (%.2f pct)"%(count_unique, count_unique*100.0/count_total, count_multi, count_xcross, count_xcross*100.0/count_total)
