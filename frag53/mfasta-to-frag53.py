#!/usr/bin/env python
import os
import sys

filename_fa = sys.argv[1]
frag_length = int(sys.argv[2])

f_fa = open(filename_fa,'r')
f_out = open('%s_53frag%d'%(filename_fa,frag_length),'w')
for line in f_fa:
    if( line.startswith('>') ):
        tmp_h = line.strip()
        tmp_seq = f_fa.next().strip()

        f_out.write('%s_5\n%s\n'%(tmp_h,tmp_seq[:frag_length]))
        f_out.write('%s_3\n%s\n'%(tmp_h,tmp_seq[-1*frag_length:]))
f_out.close()
f_fa.close()
