#!/usr/bin/python
import os
import sys
import gzip

usage_mesg = 'Usage: qual2pos_qual.py <.qual file>'

if(len(sys.argv)!=2):
    print(usage_mesg)
    sys.exit(1)

filename_qual = sys.argv[1]
if( not os.access(filename_qual,os.R_OK) ):
    print("%s is not accessible"%filename_qual)
    print(usage_mesg)
    sys.exit(1)

qscore_list = range(-1,41)
filename_out = filename_qual.replace('qual','')+'pos_qual'

f_qual = open(filename_qual,'r')
if( filename_qual.endswith('.gz') ):
    filename_out = filename_qual.replace('qual.gz','')+'pos_qual'
    f_qual = gzip.open(filename_qual,'rb')

count_nocall = 0
count_total = 0
pos_qual_map = dict()
read_len = 0
for line in f_qual:
    if(line.startswith('#')):
        continue
    if( line.startswith('>')):
        count_total += 1
        h = line.strip()
        tokens_q = f_qual.next().strip().split()
        if( '-1' in tokens_q ):
            count_nocall += 1
            continue
        if( read_len == 0 ):
            read_len = len(tokens_q)
            for pos in range(0,read_len):
                pos_qual_map[pos] = dict()
                for tmp_qual in qscore_list:
                    pos_qual_map[pos][tmp_qual] = 0

        for pos in range(0,read_len):
            pos_qual_map[pos][int(tokens_q[pos])] += 1
f_qual.close()

f_out = open(filename_out,'w')
f_out.write('Qscore\t'+"\t".join(['%d'%x for x in qscore_list])+"\n")
for pos in range(0,read_len):
    f_out.write('%d\t%s\n'%(pos,'\t'.join(['%d'%pos_qual_map[pos][x] for x in qscore_list])))
f_out.write('#Total reads: %d\n'%count_total)
f_out.write('#Reads with nocall: %d\n'%count_nocall)
f_out.close()
