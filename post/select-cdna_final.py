#!/usr/bin/python
import os
import sys

filename_final = sys.argv[1]
filename_nr = sys.argv[2]

h_nr = ''
seq_nr = dict()
f_nr = open(filename_nr,'r')
for line in f_nr:
    if( line.startswith('>') ):
        h_nr = line.strip()
        seq_nr[h_nr] = []
    else:
        seq_nr[h_nr].append( line.strip() )
f_nr.close()

f_final = open(filename_final,'r')
for line in f_final:
    if( line.startswith('>') ):
        tmp_h = line.strip()
        if( seq_nr.has_key(tmp_h) ):
            print "%s\n%s"%(tmp_h,''.join(seq_nr[tmp_h]))
f_final.close()
