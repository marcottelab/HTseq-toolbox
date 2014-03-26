#!/usr/bin/env python
import os
import sys

filename_tf = sys.argv[1]
filename_fa = sys.argv[2]

seqlen = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seqlen[seq_h] = 0
    else:
        seqlen[seq_h] += len(line.strip())
f_fa.close()

raw_freq = dict()
f_tf = open(filename_tf,'r')
for line in f_tf:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    raw_freq[ tokens[0] ] = int(tokens[1])
f_tf.close()

sum_freq = sum(raw_freq.values())
f_out = open('%s.rpkm'%filename_tf.replace('.t_freq',''),'w')
f_out.write('#Total read count: %d\n'%sum_freq)
f_out.write('#SeqID\tRPKM\tRawCount\tSeqLen\n')
for tmp_h in sorted(raw_freq.keys(),key=raw_freq.get,reverse=True):
    tmp_rpkm = raw_freq[tmp_h]*1000000.0/sum_freq*1000.0/seqlen[tmp_h]
    f_out.write('%s\t%.2f\t%d\t%d\n'%(tmp_h,tmp_rpkm,raw_freq[tmp_h],seqlen[tmp_h]))
f_out.close()
