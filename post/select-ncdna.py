#!/usr/bin/python
import os
import sys

filename_nrC = sys.argv[1]
filename_cdna = sys.argv[2]

def fa2seq(filename):
    rv = dict()
    tmp_h = ''
    f = open(filename,'r')
    for line in f:
        if( line.startswith('>') ):
            tmp_h = line.strip().lstrip('>')
            rv[tmp_h] = []
        else:
            rv[tmp_h].append( line.strip() )
    f.close()
    return rv

nrC_list = fa2seq(filename_nrC)
cdna_list = fa2seq(filename_cdna)

filename_base = filename_cdna.replace('_cdna.fa','')
sample_name = filename_base.replace('_XENLA','')

idx = 1
f_out = open('%s_ncdna.fa'%filename_base,'w')
f_raw= open('%s_ncdna.raw.fa'%filename_base,'w')
for tmp_h in sorted(nrC_list.keys()):
    if( not cdna_list.has_key(tmp_h) ):
        tmp_seq = ''.join(nrC_list[tmp_h])
        f_raw.write('>%s\n%s\n'%(tmp_h,tmp_seq))
        f_out.write('>%s_nc_%08d\n%s\n'%(sample_name,idx,tmp_seq))
        idx += 1
f_out.close()
f_raw.close()
