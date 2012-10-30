#!/usr/bin/env python
import os
import sys

filename_fa = sys.argv[1]

sample_name = '_'.join(os.path.basename(filename_fa).split('_')[:3]).replace('_XENLA','')

f = open(filename_fa,'r')
for line in f:
    if( line.startswith('>') ):
        tokens = line.strip().split("_")
        print ">%s_%s_%s"%(sample_name,tokens[1],tokens[3])
    else:
        print line.strip()
f.close()
