#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

og2oTx = dict()
f_list = open('Taira201203_XENLA_tissue_pep_final.nr_gene_list','r')
for line in f_list:
    tokens = line.strip().split("\t")
    oTx_id = tokens[0]
    og_id = "%s.%s"%(tokens[1],tokens[2])
    if( not og2oTx.has_key(og_id) ):
        og2oTx[og_id] = []
    og2oTx[og_id].append(oTx_id)
f_list.close()

seq_list = dict()
seq_h = ''
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()

for tmp_og in sorted(og2oTx.keys()):
    longest_oTx = ''
    longest_len = 0
    longest_seq = ''
    for tmp_oTx in sorted(og2oTx[tmp_og]):
        tmp_seq = ''.join(seq_list[tmp_oTx])
        #print ">%s.%s\n%s"%(tmp_oTx,tmp_og,tmp_seq)
        if( len(tmp_seq) > longest_len ):
            longest_oTx = tmp_oTx
            longest_seq = tmp_seq

    print ">%s.%s\n%s"%(longest_oTx,tmp_og,longest_seq)
