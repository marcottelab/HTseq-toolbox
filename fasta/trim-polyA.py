#!/usr/bin/python
import os
import sys
import re

filename_fa = sys.argv[1]

h_fa = ''
seq_list = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        h_fa = line.strip()
        seq_list[h_fa] = []
    else:
        seq_list[h_fa].append( line.strip() )
f_fa.close()

for tmp_h in seq_list.keys():
    tmp_seq = ''.join(seq_list[tmp_h])
    if( re.search('A{6,}$',tmp_seq) != None ):
        new_seq = re.sub('A{6,}$','AAAAAA',tmp_seq)
        print "%s\n%s"%(tmp_h,new_seq)
    else:
        print "%s\n%s"%(tmp_h,tmp_seq)
