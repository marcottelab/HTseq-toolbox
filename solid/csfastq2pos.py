#!/usr/bin/python
import os
import sys
import gzip

filename_fastq = sys.argv[1]
filename_base = filename_fastq.replace('.fastq','')
f_fastq = open(filename_fastq,'r')
if( filename_fastq.endswith('.gz') ):
    f_fastq = gzip.open(filename_fastq,'rb')
    filename_base = filename_fastq.replace('.fastq.gz','')

n_freq = dict()
q_freq = dict()

read_len = 0
for line in f_fastq:
    if( line.startswith('@') ):
        nseq = f_fastq.next().strip()
        f_fastq.next()
        qseq = f_fastq.next().strip()
        if( read_len == 0 ):
            read_len = len(nseq)
        
        for tmp_pos in range(1,read_len):
            tmp_n = nseq[tmp_pos]
            if( not n_freq.has_key(tmp_n) ):
                n_freq[tmp_n] = dict()
            if( not n_freq[tmp_n].has_key(tmp_pos) ):
                n_freq[tmp_n][tmp_pos] = 0
            n_freq[tmp_n][tmp_pos] += 1
            
            tmp_q = qseq[tmp_pos-1]
            if( not q_freq.has_key(tmp_q) ):
                q_freq[tmp_q] = dict()
            if( not q_freq[tmp_q].has_key(tmp_pos) ):
                q_freq[tmp_q][tmp_pos] = 0
            q_freq[tmp_q][tmp_pos] += 1
f_fastq.close()

q_list = sorted([ord(x)-32 for x in q_freq.keys()])
n_list = sorted(n_freq.keys())

f_qout = open('%s.pos_qual'%filename_base,'w')
f_qout.write('Pos\t%s\n'%('\t'.join(['%d'%x for x in q_list])))
for tmp_pos in range(1,read_len):
    tmp_q_list = []
    for tmp_q in q_list:
        tmp_qchar = chr(tmp_q+32)
        if( q_freq[tmp_qchar].has_key(tmp_pos) ):
            tmp_q_list.append( q_freq[tmp_qchar][tmp_pos] )
        else:
            tmp_q_list.append(0)
    f_qout.write('%d\t%s\n'%(tmp_pos, '\t'.join(["%d"%x for x in tmp_q_list])))
f_qout.close()

f_nout = open('%s.pos_call'%filename_base,'w')
f_nout.write('Pos\t%s\n'%('\t'.join(n_list)))
for tmp_pos in range(1,read_len):
    tmp_n_list = []
    for tmp_n in n_list:
        if( n_freq[tmp_n].has_key(tmp_pos) ):
            tmp_n_list.append( n_freq[tmp_n][tmp_pos] )
        else:
            tmp_n_list.append(0)
    f_nout.write('%d\t%s\n'%(tmp_pos, '\t'.join(['%d'%x for x in tmp_n_list])))
f_nout.close()
