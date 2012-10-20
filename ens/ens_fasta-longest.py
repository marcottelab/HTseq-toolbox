#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

seq_list = dict()
seq_h = ''
gene2seq = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        gene_id = seq_h.split('|')[-1]
        seq_list[seq_h] = []
        if( not gene2seq.has_key(gene_id) ):
            gene2seq[gene_id] = []
        gene2seq[gene_id].append(seq_h)
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()

for tmp_gene in sorted(gene2seq.keys()):
    h_longest = ''
    seq_longest = ''
    for tmp_h in gene2seq[tmp_gene]:
        tmp_seq = ''.join(seq_list[tmp_h])
        if( h_longest == '' ):
            h_longest = tmp_h
            seq_longest = tmp_seq
            continue
            
        if( len(seq_longest) < len(tmp_seq) ):
            h_longest = tmp_h
            seq_longest = tmp_seq

    print ">%s %s %d\n%s"%(tmp_gene,h_longest,len(gene2seq[tmp_gene]),seq_longest)

