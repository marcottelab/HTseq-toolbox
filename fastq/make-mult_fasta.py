#!/usr/bin/python
import os
import sys
import gzip

filename_rf = sys.argv[1]
read_prefix = filename_rf.split(".")[0]

total_reads = 0
total_readcounts = 0
single_reads = 0
lt10_reads = 0
lt10_readcounts = 0

f_rf = open(filename_rf,'r')
f_mout = open("%s.mult_fasta"%read_prefix,'w')
if( filename_rf.endswith('.gz') ):
    f_rf = gzip.open(filename_rf,'rb')

idx = 0
for line in f_rf:
    tokens = line.strip().split()
    tmp_count = int(tokens[0])
    total_reads += 1
    total_readcounts += tmp_count
    if( tmp_count == 1 ):
        single_reads += 1
        lt10_reads += 1
        lt10_readcounts += 1
    else:
        f_mout.write(">%s_%08d_%d\n%s\n"%(read_prefix,idx,tmp_count,tokens[1]))
        idx += 1
        if( tmp_count < 10 ):
            lt10_reads += 1
            lt10_readcounts += tmp_count
f_rf.close()
f_mout.close()

f_log = open("%s.mult_fasta.log"%read_prefix,'w')
f_log.write("Reads: total=%d, single=%d(%.3f), lt10=%d(%.3f))\n"%(total_reads,single_reads,float(single_reads)/total_reads,lt10_reads,float(lt10_reads)/total_reads))
f_log.write("ReadCounts: total=%d, single=%d(%.3f), lt10=%d(%.3f)\n"%(total_readcounts,single_reads,float(single_reads)/total_readcounts, lt10_readcounts, float(lt10_readcounts)/total_readcounts))
f_log.close()
