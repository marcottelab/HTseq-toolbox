#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_sam = sys.argv[1]
filename_hit = filename_sam+'_hit'
filename_nohit = filename_sam+'_nohit'

f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')
    filename_sam = re.sub('.gz$','',filename_sam)

    filename_hit = filename_sam+'_hit'
    filename_nohit = filename_sam+'_nohit'

f_hit = open(filename_hit,'w')
f_nohit = open(filename_nohit,'w')
for line in f_sam:
    if( line.startswith('@') ):
        f_hit.write('%s\n'%line.strip())
        continue

    tokens = line.strip().split("\t")
    if( tokens[2] == '*' ):
        f_nohit.write('@%s\n'%(tokens[0]))
        continue
    f_hit.write('%s\n'%line.strip())
f_sam.close()
f_hit.close()
f_nohit.close()
