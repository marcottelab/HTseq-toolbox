#!/usr/bin/python
import os
import sys
import gzip

usage_mesg = 'Usage: csfasta2pos_cs.py <.csfastafile>'

if(len(sys.argv)!=2):
    print(usage_mesg)
    sys.exit(1)

filename_csfasta = sys.argv[1]
if( not os.access(filename_csfasta,os.R_OK) ):
    print("%s is not accessible"%filename_csfasta)
    print(usage_mesg)
    sys.exit(1)

cs_list = ['0','1','2','3']
filename_out = filename_csfasta.replace('.csfasta','')+'pos_cs'

f_csfasta = open(filename_qual,'r')
if( filename_csfasta.endswith('.gz') ):
    filename_out = filename_csfasta.replace('.csfasta.gz','')+'pos_cs'
    f_csfasta = gzip.open(filename_csfasta,'rb')

count_nocall = 0
count_total = 0
pos_csfasta_map = dict()
read_len = 0
for line in f_csfasta:
    if(line.startswith('#')):
        continue
    if( line.startswith('>')):
        count_total += 1
        h = line.strip()
        tokens_cs = f_csfasta.next().strip().split('')
        if( '.' in tokens_cs ):
            count_nocall += 1
            continue
        if( read_len == 0 ):
            read_len = len(tokens_cs)
            for pos in range(0,read_len):
                pos_csfasta_map[pos] = dict()
                for tmp_cs in cs_list:
                    pos_csfasta_map[pos][tmp_cs] = 0

        for pos in range(0,read_len):
            pos_csfasta_map[pos][tokens_cs[pos]] += 1
f_csfasta.close()

f_out = open(filename_out,'w')
f_out.write('Qscore\t'+"\t".join(['%d'%x for x in qscore_list])+"\n")
for pos in range(0,read_len):
    f_out.write('%d\t%s\n'%(pos,'\t'.join(['%d'%pos_csfasta_map[pos][x] for x in qscore_list])))
f_out.write('#Total reads: %d\n'%count_total)
f_out.write('#Reads with nocall: %d\n'%count_nocall)
f_out.close()
