#!/usr/bin/python
import os
import sys
import gzip

filename_csfasta = sys.argv[1]
filename_old = '_old_%s'%(filename_csfasta)
os.rename(filename_csfasta,filename_old)

f_csfasta = open(filename_old,'r')
if( filename_csfasta.endswith('.gz') ):
    f_csfasta = gzip.open(filename_old,'rb')
f_out = open(filename_csfasta.replace('.gz',''),'w')

for line in f_csfasta:
    if( line.startswith('>') ):
        f_out.write('%s\n'%(line.strip().split(':')[0]))
    else:
        f_out.write('%s\n'%(line.strip()))
f_out.close()
f_csfasta.close()
