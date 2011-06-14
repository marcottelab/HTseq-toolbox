#!/usr/bin/python
import os
import sys
import gzip

filename_sam = sys.argv[1]
filename_out = filename_sam+'_slim'

f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')
    filename_out = filename_sam.replace('.gz','')+'_slim'

f_out = open(filename_out,'w')
for line in f_sam:
    if( line.startswith('@') ):
        f_out.write('%s\n'%line.strip())
        continue

    tokens = line.strip().split("\t")
    if( tokens[2] == '*' ):
        continue
    f_out.write('%s\n'%"\t".join(tokens))
f_sam.close()
f_out.close()
