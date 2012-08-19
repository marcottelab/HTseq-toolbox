#!/usr/bin/env python
import os
import sys
import gzip

filename_rf = sys.argv[1]
read_prefix = filename_rf.split(".")[0]

f_rf = open(filename_rf,'r')
if( filename_rf.endswith('.gz') ):
    f_rf = gzip.open(filename_rf,'rb')

read_freq = dict()
for line in f_rf:
    tokens = line.strip().split()
    tmp_count = int(tokens[0])
    tmp_seq = tokens[1]
    if( not read_freq.has_key(tmp_seq) ):
        read_freq[tmp_seq] = 0
    read_freq[tmp_seq] += tmp_count
f_rf.close()

count_single = 0
count_total = 0 

f_out = open('%s.norm_fasta'%read_prefix,'w')
idx = 0
for tmp_seq in sorted(read_freq.keys(),key=read_freq.get):
    if( read_freq[tmp_seq] == 1 ):
        count_single += 1
    count_total += read_freq[tmp_seq]
    f_out.write('>%s_%08d_%d\n%s\n'%(read_prefix,idx,read_freq[tmp_seq],tmp_seq))
    idx += 1
f_out.close()

count_reads = len(read_freq.keys())
f_log = open("%s.norm_fasta_log"%read_prefix,'w')
f_log.write("Reads: total=%d, single=%d(%.3f)\n"%(count_reads, count_single, float(count_single)/count_reads))
f_log.write("ReadCounts: total=%d, single=%d(%.3f)\n"%(count_total, count_single, float(count_single)/count_total))
f_log.close()
