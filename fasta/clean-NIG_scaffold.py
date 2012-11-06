#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

seq_h = ''
seq_list = dict()
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        if( line.startswith('>scaffold') ):
            seq_num = int(line.strip().split()[0].replace('>scaffold',''))
            seq_h = '>NIGv1.S%08d'%seq_num
        else:
            seq_h = '>NIGv1.%s'%line.strip().split()[0].lstrip('>')
        seq_list[ seq_h ] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()

for tmp_h in sorted(seq_list.keys()):
    tmp_seq = ''.join(seq_list[tmp_h])
    tmp_set = set(tmp_seq) - set(['A','T','G','C'])
    print "%s\n%s"%(tmp_h,tmp_seq)
