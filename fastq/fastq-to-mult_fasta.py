#!/usr/bin/env python
import os
import sys

filename_fq = sys.argv[1]
base_name = filename_fq.replace('.fastq','').replace('.called','')

seq_count = dict()
f_fq = open(filename_fq,'r')
for line in f_fq:
    if( line.startswith('@') ):
        h = line.strip().split()[0]
        nseq = f_fq.next().strip()
        qh = f_fq.next()
        qseq = f_fq.next().strip()
        if( not seq_count.has_key(nseq) ):
            seq_count[nseq] = 0
        seq_count[nseq] += 1
f_fq.close()

seq_idx = 0
count_mult = 0
count_single = 0
freq_mult = 0
freq_single = 0
f_mult = open('%s.mult_fasta'%base_name,'w')
f_single = open('%s.single_fasta'%base_name,'w')
for tmp_nseq in sorted(seq_count.keys(),key=seq_count.get):
    out_str = ">%s_%09d_%d\n%s\n"%(base_name,seq_idx,seq_count[tmp_nseq],tmp_nseq)
    if( seq_count[tmp_nseq] > 1 ):
        f_mult.write(out_str)
        freq_mult += seq_count[tmp_nseq]
        count_mult += 1
    else:
        f_single.write(out_str)
        freq_single += seq_count[tmp_nseq]
        count_single += 1
    seq_idx += 1
f_mult.close()
f_single.close()

f_log = open('%s.mult_fasta.log'%base_name,'w')
count_total = len(seq_count.values())
freq_total = sum(seq_count.values())
f_log.write('Total reads: %d (freq: %d)\n'%(count_total,freq_total))
f_log.write('Mult reads: %d %.3f (freq:%d %.3f)\n'%(count_mult,float(count_mult)/count_total,freq_mult,float(freq_mult)/count_mult))
f_log.write('Single reads: %d (freq:%d)\n'%(count_single,freq_single))
f_log = open('%s.mult_fasta.log'%base_name,'w')
