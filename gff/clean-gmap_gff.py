#!/usr/bin/env python
import os
import sys

filename_gff = sys.argv[1]

print "##gff-version 3"
f_gff = open(filename_gff,'r')
for line in f_gff:
    if( line.startswith('#') ):
        continue

    tokens = line.strip().split("\t")
    t_id = tokens[0]
    if( t_id.find(';;') >= 0 ):
        t_tokens = t_id.split('.')
        tokens[0] = '%s.%s.chrNA'%(t_tokens[0],t_tokens[1])

    new_attr_list = []
    tmp_path_no = 0
    for tmp_attr in tokens[8].split(';'):
        if( tmp_attr.startswith('ID=') ):
            tmp_path_no = int(tmp_attr.split('.')[-1][-1])
            new_attr_list.append( tmp_attr )
        elif( tmp_attr.startswith('Name=') ):
            new_attr_list.append( tmp_attr.split('|')[0] )
        elif( tmp_attr.startswith('Parent=') ):
            tmp_path_no = int(tmp_attr.split('.')[-1][-1])
            new_attr_list.append( tmp_attr )
        else:
            new_attr_list.append( tmp_attr )
    if( tmp_path_no > 1 ):
        continue

    tokens[8] = ';'.join(new_attr_list)
    print "\t".join(tokens)
f_gff.close()

