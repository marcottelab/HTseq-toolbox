#!/usr/bin/env python
import os
import sys

filename_prot_final = sys.argv[1]
filename_cdna_NR = sys.argv[2]

prot_list = dict()
f_prot_final = open(filename_prot_final,'r')
for line in f_prot_final:
    if( line.startswith('>') ):
        tmp_h = line.strip().replace('>Mp.','').replace('>p.','')
        prot_list[ tmp_h ] = 1
f_prot_final.close()

data_name = filename_prot_final.split('.')[0]

is_print = 0
f_cdna_final = open('%s.cdna_final.fa'%data_name,'w')
f_cdna_NR = open(filename_cdna_NR,'r')
for line in f_cdna_NR:
    if( line.startswith('>') ):
        tmp_h = line.strip().replace('>c.','')
        if( prot_list.has_key(tmp_h) ):
            is_print = 1
            f_cdna_final.write('%s\n'%line.strip())
        else:
            is_print = 0
    elif( is_print > 0 ):
        f_cdna_final.write('%s\n'%line.strip())
f_cdna_NR.close()
f_cdna_final.close()
