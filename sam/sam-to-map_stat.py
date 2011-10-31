#!/usr/bin/python
import os
import sys

filename_sam = sys.argv[1]

read_list = []
perfect_read_list = []
target_list = []
f_sam = open(filename_sam,'r')
for line in f_sam:
    if( line.startswith('@') ):
        continue
    tokens = line.strip().split("\t")
    read_list.append( tokens[0] )
    target_list.append( tokens[2] )
    if( tokens[5].find('I') < 0 and tokens[5].find('D') < 0 ):
        perfect_read_list.append(tokens[0])
f_sam.close()

print "Total hits: ",len(read_list)
print "Total targets: ",len(list(set(target_list)))
print "Total reads: ",len(list(set(read_list)))
print "Total perfectly matched reads: ",len(list(set(perfect_read_list)))
