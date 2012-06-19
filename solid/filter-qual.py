#!/usr/bin/python
import os 
import sys
import gzip

usage_mesg = 'Usage: filter-qual.py <_QV.qual file>'

if(len(sys.argv) != 2):
    print usage_mesg
    sys.exit(1)

filename_qual = sys.argv[1]
if( not os.access(filename_qual,os.R_OK) ):
    print "%s is not accessible"%filename_qual
    print usage_mesg
    sys.exit(1)

count_all = 0
count_nocall = 0
count_minQ15 = 0
count_avgQ15 = 0

h = ''
filename_base = filename_qual.replace('_QV.qual','')
f_nocall = open(filename_base+'.nocall','w')
f_minQ15 = open(filename_base+'.minQ15','w')
f_avgQ15 = open(filename_base+'.avgQ15','w')

f_qual = open(filename_qual,'r')
if( filename_qual.endswith('.gz') ):
    f_qual = gzip.open(filename_qual,'rb')

for line in f_qual:
    if(line.startswith('#')):
        continue
    
    if(line.startswith('>')):
        count_all += 1
        h = line.strip()
    else:
        qstr = line.strip()
        qtokens = qstr.split()

        min_qscore = 40
        sum_qscore = 0
        has_nocall = 0
        for tmp_q in qtokens:
            nq = int(tmp_q)
            sum_qscore += nq 
            if( nq < 0 ):
                has_nocall += 1
            if( nq < min_qscore ):
                min_qscore = nq 
        if( has_nocall > 0 ):
            count_nocall += 1
            f_nocall.write("%s\n%s\n"%(h,qstr))
        else:
            if( min_qscore >= 15 ):
                count_minQ15 += 1
                f_minQ15.write("%s\n%s\n"%(h,qstr))
            avg_qscore = float(sum_qscore/len(qtokens))
            if( avg_qscore >= 15 ):
                count_avgQ15 += 1
                f_avgQ15.write("%s\n%s\n"%(h,qstr))
f_qual.close()
f_nocall.close()
f_minQ15.close()
f_avgQ15.close()

sys.stderr.write("Filename: %s\n"%filename_qual)
sys.stderr.write("Total reads: %d\n"%count_all)
sys.stderr.write("Reads with no call: %d\n"%count_nocall)
sys.stderr.write("Reads with min. Qscore >= 15 : %d\n"%count_minQ15)
sys.stderr.write("Reads with avg. Qscore >= 15 : %d\n"%count_avgQ15)

f_log = open(filename_qual+'.log','a')
f_log.write("\nScript: %s\n"%usage_mesg)
f_log.write("Filename: %s\n"%filename_qual)
f_log.write("Total reads: %d\n"%count_all)
f_log.write("Reads with no call: %d\n"%count_nocall)
f_log.write("Reads with min. Qscore >= 15 : %d\n"%count_minQ15)
f_log.write("Reads with avg. Qscore >= 15 : %d\n"%count_avgQ15)
f_log.close()
