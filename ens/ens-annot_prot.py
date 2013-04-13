#!/usr/bin/python
import os
import sys

filename_names = sys.argv[1]
filename_prot = sys.argv[2]

names = dict()
f_names = open(filename_names,'r')
f_names.readline()
for line in f_names:
    tokens = line.split("\t")
    names[tokens[0]] = tokens[1].strip()
f_names.close()

f_prot = open(filename_prot,'r')
for line in f_prot:
    if( line.startswith('>') ):
        tokens = line.strip().lstrip('>').split('|')
        gene_id = tokens[-1]
        if( names.has_key(gene_id) ):
            print ">%s|%s"%(names[gene_id],'|'.join(tokens))
        else:
            print ">NA|%s"%(names[gene_id],'|'.join(tokens))
    else:
        print line.strip()
f_prot.close()
