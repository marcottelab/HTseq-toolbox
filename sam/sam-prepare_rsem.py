#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_sam = sys.argv[1]
filename_base = re.sub(r'.sam[A-z_]*[.gz]*','',filename_sam)

f_sam= open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')

count_good = 0
count_filtered = 0
filtered_reads = dict()
for line in f_sam:
    if( line.startswith('@') and len(line.split()[0]) < 5 ):
        continue

    tokens = line.strip().split("\t")
    tmp_cigar = tokens[5]
    tmp_flag = int(tokens[1])
    if( tmp_flag & 1 ):
        if( tmp_flag & 8 or tmp_flag & 4 ):
            filtered_reads[ tokens[0] ] = 1
            count_filtered += 1
            continue
        if( line.find('XA:Z:') > 0 ):
            filtered_reads[ tokens[0] ] = 1
            count_filtered += 1
            continue
    if( tokens[6] != '=' ):
        filtered_reads[ tokens[0] ] = 1
        count_filtered += 1
        continue
    if( tmp_cigar.find('I') >= 0 or tmp_cigar.find('D') >= 0 ):
        filtered_reads[ tokens[0] ] = 1
        count_filtered += 1
        continue
    if( tmp_cigar.find('S') >= 0 or tmp_cigar.find('H') >= 0 or tmp_cigar.find('N') >= 0 ):
        filtered_reads[ tokens[0] ] = 1
        count_filtered += 1
        continue
    count_good += 1
f_sam.close()

sys.stderr.write('Filtered: %d\n'%len(filtered_reads))
f_sam= open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')

for line in f_sam:
    tokens = line.strip().split("\t")
    if( filtered_reads.has_key(tokens[0]) ):
        continue

    print line.strip()
f_sam.close()
sys.stderr.write('%s - filtered: %d (%d reads)  good: %d\n'%(filename_sam, count_filtered, len(filtered_reads), count_good))
