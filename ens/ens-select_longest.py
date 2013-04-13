#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

seq_h = ''
seq_list = dict()

f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append(line.strip())
f_fa.close()

longest = dict()
for tmp_h in seq_list.keys():
    tmp_gene = tmp_h.split('|')[1]
    tmp_seq = ''.join(seq_list[tmp_h])
    if( not longest.has_key(tmp_gene) ):
        longest[tmp_gene] = {'id':tmp_h, 'seq':tmp_seq}
    elif( len(tmp_seq) > len(longest[tmp_gene]['seq']) ):
        longest[tmp_gene] = {'id':tmp_h, 'seq':tmp_seq}

for tmp_gene in longest.keys():
    print ">%s\n%s"%(longest[tmp_gene]['id'], longest[tmp_gene]['seq'])
