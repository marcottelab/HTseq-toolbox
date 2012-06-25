#!/usr/bin/python
import os
import sys

filename_pep_final = sys.argv[1]
filename_cdna = sys.argv[2]

cdna_list = dict()
cdna_h = ''
f_cdna = open(filename_cdna,'r')
for line in f_cdna:
    if( line.startswith('>') ):
        cdna_h = line.strip()
        cdna_list[cdna_h] = []
    else:
        cdna_list[cdna_h].append( line.strip() )
f_cdna.close()

f_pep = open(filename_pep_final,'r')
for line in f_pep:
    if( line.startswith('>') ):
        tmp_h = line.strip()
        print "%s\n%s"%( tmp_h, ''.join( cdna_list[tmp_h] ) )
f_pep.close()
