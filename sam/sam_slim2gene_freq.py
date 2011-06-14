#!/usr/bin/python
import os
import sys

tx2gene = dict()
f_list = open('DB_headers.txt','r')
for line in f_list:
    tokens = line.strip().split()
    tx_id = tokens[0].lstrip('>')
    gene_id = tokens[3].replace('gene:','')
    #print gene_id,tx_id
    tx2gene[tx_id] = gene_id
f_list.close()

gene_freq = dict()
filename_sam = sys.argv[1]
f_sam = open(filename_sam,'r')
for line in f_sam:
    if(line.startswith('@') ): 
        continue
    tokens = line.strip().split("\t")
    if( tokens[2] != '*' ):
        if( not tx2gene.has_key(tokens[2]) ):
            sys.stderr.write('No Gene ID: %s\n'%(tokens[2]))
            continue
        gene_id = tx2gene[tokens[2]]
        if( not gene_freq.has_key(gene_id) ):
            gene_freq[gene_id] = 0
        gene_freq[gene_id] += 1
f_sam.close()

for gene_id in sorted(gene_freq.keys(),key=gene_freq.get,reverse=True):
    print gene_freq[gene_id],gene_id
