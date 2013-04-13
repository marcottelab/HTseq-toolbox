#!/usr/bin/python
import os
import sys

filename_names = sys.argv[1]
filename_prot = sys.argv[2]
filename_cdna = sys.argv[3]

names = dict()
f_names = open(filename_names,'r')
f_names.readline()
for line in f_names:
    tokens = line.split("\t")
    names[tokens[0]] = tokens[1].strip().replace(' ','').replace('(','_').replace(')','_').upper()
f_names.close()

coding = dict()
f_prot = open(filename_prot,'r')
for line in f_prot:
    if( line.startswith('>') ):
        tokens = line.strip().split('|')
        coding[ tokens[1] ] = tokens[0]
f_prot.close()

is_print = 0
f_cdna = open(filename_cdna,'r')
for line in f_cdna:
    if( line.startswith('>') ):
        tokens = line.strip().lstrip('>').split('|')
        g_id = tokens[1]
        tx_id = tokens[0]
        if( not names.has_key(g_id) ):
            is_print = 0
        else:
            is_print = 1

        if( is_print > 0 ):
            tmp_name = 'NA'
            if( names[g_id] != '' ):
                tmp_name = names[g_id]
            is_coding = 'coding'
            if( not coding.has_key(tx_id) ):
                is_coding = 'non-coding'
            print ">%s|%s|%s|%s"%(tmp_name,g_id,tx_id,is_coding)
    else:
        if( is_print > 0 ):
            print line.strip()
f_cdna.close()
