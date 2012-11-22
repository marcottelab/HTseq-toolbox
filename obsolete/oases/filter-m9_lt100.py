#!/usr/bin/python
import os
import sys

filename_m9 = sys.argv[1]
f_out = open('%s.lt100'%filename_m9,'w')
f_m9 = open(filename_m9,'r')
for line in f_m9:
    if( line.startswith('#') ):
        f_out.write(line)
    else:
        tokens = line.strip().split("\t")
        align_len = int(tokens[3])
        if( align_len > 100 ):
            f_out.write(line)
f_m9.close()
f_out.close()
