#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_fa = sys.argv[1]

f_fa = open(filename_fa,'r')
if( filename_fa.endswith('.gz') ):
    f_fa = gzip.open(filename_fa,'rb')

sys.stderr.write('Read %s ... '%filename_fa)
seq_h = ''
seq_list = dict()
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_fa.close()
sys.stderr.write('Done\n')

f_out = open('%s.N_dist'%(re.sub(r'.fa[sta]*','',filename_fa)),'w')
f_out.write('#SeqID\tNsLen\tNsStart\tNsEnd\n')
for tmp_h in seq_list.keys():
    tmp_seq = ''.join(seq_list[tmp_h])
    for tmp_n in re.finditer(r'N+',tmp_seq):
        tmp_start = tmp_n.start()
        tmp_end = tmp_n.end()
        tmp_len = tmp_end - tmp_start
        f_out.write("%s\t%d\t%d\t%d"%(tmp_h,tmp_len,tmp_start,tmp_end))
f_out.close()
