#!/usr/bin/env python
import os
import sys
import gzip
import re

filename_sam = sys.argv[1]
filename_base = filename_sam

f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')
    filename_base = re.sub(r'.gz$','',filename_base)

f_best = open('%s_best'%filename_base,'w')
f_dubious = open('%s_dubious'%filename_base,'w')

read_freq = dict()
for line in f_sam:
    if( line.startswith('@') and len(line.split()[0]) < 4 ):
        f_best.write(line)
        f_dubious.write(line)
        continue
    tokens = line.strip().split("\t")
    tmp_pair = 1
    if( tokens[1] & 128 ):
        tmp_pair = 2
    read_id = '%s|%d'%(tokens[0],tmp_pair)

    t_id = tokens[2]
    if( t_id == '*' ):
        continue
    mapq = int(tokens[4])

    if( not read_freq.has_key(read_id) ):
        read_freq[read_id] = dict()
    if( not read_freq[read_id].has_key(mapq) ):
        read_freq[read_id][mapq] = []
    
    if( len(read_freq[read_id][mapq]) > 2 ):
        continue
    read_freq[read_id][mapq].append( line )
f_sam.close()

count_best = 0
count_dubious = 0
for read_id in sorted(read_freq.keys()):
    best_mapq = sorted(read_freq[read_id].keys(), key=read_freq[read_id].get, reverse=True)[0]
    if( len(read_freq[read_id][best_mapq]) == 1 ):
        if( best_mapq > 0 ):
            f_best.write(read_freq[read_id][best_mapq][0])
            count_best += 1
        else:
            f_dubious.write(read_freq[read_id][best_mapq][0])
            count_dubious += 1
    else:
        count_dubious += 1
        for tmp in read_freq[read_id][best_mapq]:
            f_dubious.write(tmp)
f_best.close()
f_dubious.close()

sys.stderr.write('%s - Total %d, Best %d, Dubious %d\n'%(filename_sam,count_best+count_dubious,count_best,count_dubious))
