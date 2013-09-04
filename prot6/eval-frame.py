#!/usr/bin/env python
import os
import sys

data_name = sys.argv[1]

total_coding = 0
total_noncoding = 0
query_list = []
f_fa = open('%s.fa'%data_name,'r')
for line in f_fa:
    if( line.startswith('>') ):
        tmp_h = line.strip().lstrip('>')
        is_coding = tmp_h.split('|')[3]
        query_list.append( tmp_h )
        if( is_coding == 'coding' ):
            total_coding += 1
        else:
            total_noncoding += 1
f_fa.close()

eval_list = []
count_noncoding_correct = 0
count_noncoding_incorrect = 0
f_dubious = open('%s.dubious_frame'%data_name,'r')
for line in f_dubious:
    tokens = line.strip().split("\t")
    eval_list.append(tokens[0])
    is_coding = tokens[0].split('|')[-1]
    if( is_coding == 'non-coding' ):
        count_noncoding_correct += 1
    else:
        count_noncoding_incorrect += 1
f_dubious.close()

f_nohit = open('%s.nohit_frame'%data_name,'r')
for line in f_nohit:
    tokens = line.strip().split("\t")
    eval_list.append(tokens[0])
    is_coding = tokens[0].split('|')[-1]
    if( is_coding == 'non-coding' ):
        count_noncoding_correct += 1
    else:
        count_noncoding_incorrect += 1
f_nohit.close()

count_coding_correct = 0
count_coding_incorrect = 0
f_unique = open('%s.unique_frame'%data_name,'r')
for line in f_unique:
    tokens = line.strip().split()[0].split("|")
    eval_list.append(tokens[0])
    is_coding = tokens[-2]
    if( is_coding == 'coding' ):
        count_coding_correct += 1
    else:
        count_coding_incorrect += 1
f_unique.close()

total_noncoding 
print "Sensitivity:", (count_coding_correct)*100.0/total_coding
print "Specificity:", (count_noncoding_correct)*100.0/total_noncoding
