#!/usr/bin/python
import os
import sys

filename_base_log = sys.argv[1]

prev_cov = -1

hole_start_cov = 0
hole_end_cov = 0
hole_start = 0
hole_end = 0
hole_cov_list = []

filename_holes = filename_base_log.replace('.base_log','')+'.holes'
f_base_log = open(filename_base_log,'r')
f_holes = open(filename_holes,'w')
f_holes100 = open(filename_holes+'100','w')
f_holes.write('#Start\tEnd\tSize\tStartCov\tEndCov\n')
f_holes100.write('#Start\tEnd\tSize\tStartCov\tEndCov\n')
for line in f_base_log:
    if( line.startswith('Pos') ):
        continue
    if( line.startswith('#') ):
        f_holes.write(line)
        f_holes100.write(line)
        continue

    tokens = line.strip().split("\t")
    tmp_pos = int(tokens[0])
    tmp_cov = int(tokens[1]) + int(tokens[2])
    if( prev_cov == -1 ):
        prev_cov = tmp_cov
        continue
    
    if( hole_start == 0 and tmp_cov == 0 ):
        hole_start_cov = prev_cov
        hole_start = tmp_pos
    
    if( hole_start > 0 and tmp_cov >= 3 ):
        hole_end = tmp_pos - 1
        hole_end_cov = tmp_cov
        f_holes.write('%d\t%d\t%d\t%d\t%d\n'%(hole_start,hole_end,hole_end-hole_start,hole_start_cov,hole_end_cov))
        if( hole_end-hole_start > 100 ):
            f_holes100.write('%d\t%d\t%d\t%d\t%d\n'%(hole_start,hole_end,hole_end-hole_start,hole_start_cov,hole_end_cov))
        
        hole_start = 0
        hole_end = 0
        hole_start_cov = 0
        hole_end_cov = 0
        hole_cov_list = []

    prev_cov = tmp_cov
f_base_log.close()
f_holes.close()
f_holes100.close()

