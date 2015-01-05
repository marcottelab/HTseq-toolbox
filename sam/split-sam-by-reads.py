#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_sam = sys.argv[1]
filename_base = re.sub(r'.sam[A-z._]*','',filename_sam)

num_reads = 10000000
if( len(sys.argv) > 2 ):
    num_reads = int(sys.argv[2])

f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')

f_h = open('%s.sam_part_h'%filename_base,'w')

f_out = dict()
f_out[0] = open('%s.sam_part_0'%filename_base,'w')

count_read = 0
prev_read = 'NA'
for line in f_sam:
    if( line.startswith('@') and len(line.split()[0]) < 4 ):
        f_h.write(line)
    else:
        tmp_read = line.split()[0].split('/')[0]
        if( tmp_read != prev_read ):
            count_read += 1
            prev_read = tmp_read
        tmp_idx = count_read/num_reads

        if( count_read % num_reads == 0 ):
            f_out[tmp_idx-1].close()
            if( not f_out.has_key(tmp_idx) ):
                f_out[tmp_idx] = open('%s.sam_part_%d'%(filename_base, tmp_idx), 'w')
            f_out[tmp_idx].write(line)
        else:
            f_out[tmp_idx].write(line)
        
f_h.close()
