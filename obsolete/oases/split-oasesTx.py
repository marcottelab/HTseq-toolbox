#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

seq_list = dict()
h_fa = ''
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        h_fa = line.strip().lstrip('>')
        seq_list[h_fa] = []
    else:
        seq_list[h_fa].append( line.strip() )
f_fa.close()

filename_base = filename_fa.replace('.oasesTx.fa','')
dir_name = "%s.raw_cls"%(filename_base)
if( not os.access(dir_name,os.R_OK) ):
    os.mkdir(dir_name)

f_single = open('%s.raw_cls_single.fa'%filename_base,'w')
for h_fa in seq_list.keys():
    tokens = h_fa.split("_")
    locus_id = tokens[1]
    tx_serial = tokens[3]
    if( tx_serial == '1/1' ):
        f_single.write('>%s\n%s\n'%(h_fa,''.join(seq_list[h_fa])))
        continue
    f_out = open( os.path.join(dir_name,'locus_%07d.fa'%int(locus_id)), 'a' )
    f_out.write('>%s\n%s\n'%(h_fa,''.join(seq_list[h_fa])))
    f_out.close()
f_single.close()
