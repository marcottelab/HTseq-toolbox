#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]
filename_list = sys.argv[2]

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
        
f_list = open(filename_list,'r')
for line in f_list:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        print ">%s\n%s"%(tmp_h,''.join(seq_list[tmp_h]))
f_list.close()
