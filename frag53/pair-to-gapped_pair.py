#!/usr/bin/env python
import os
import sys

filename_pair = sys.argv[1]
read_len = 50
perfect_cigar = '%dM'%read_len

count_perfect = 0
count_variation = 0 
count_total = 0

f_pair = open(filename_pair,'r')

f_perfect = open('%s.perfect'%filename_pair,'w')
f_variable = open('%s.variable'%filename_pair,'w')
f_gapped = open('%s.gapped'%filename_pair,'w')

for line in f_pair:
    if( line.startswith('#') ):
        continue
    
    count_total += 1
    line = line.strip()
    tokens = line.split("\t")
    target_id = tokens[1]
    tag1_list = tokens[3].split(';;')
    tag2_list = tokens[4].split(';;')
    
    is_perfect = 0
    is_variation = 0
    for tmp_tag1 in tag1_list:
        tmp_tokens1 = tmp_tag1.split('|')
        tmp_pos1 = int(tmp_tokens1[2])
        for tmp_tag2 in tag2_list:
            tmp_tokens2 = tmp_tag2.split('|')
            tmp_pos2 = int(tmp_tokens2[2])
            
            pos_diff = abs(tmp_pos1 - tmp_pos2)
            if( pos_diff == read_len and tmp_tokens1[1] == perfect_cigar and tmp_tokens2[1] == perfect_cigar ):
                is_perfect += 1
            elif( pos_diff <= read_len*2 ):
                is_variation += 1

    if( is_perfect > 0 ):
        count_perfect += 1
        f_perfect.write('%s\n'%line)
    elif( is_variation > 0 ):
        count_variation += 1
        f_variable.write('%s\n'%line)
    else:
        f_gapped.write('%s\n'%line)

    #if( is_perfect ==  0 ):
    #    print line.strip()
f_pair.close()
f_perfect.close()
f_variable.close()
f_gapped.close()

sys.stderr.write('%s - perfect:%d, variable:%d, gapped:%d\n'%(filename_pair, count_perfect, count_variation, count_total - count_perfect - count_variation))
