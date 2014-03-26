#!/usr/bin/python
import os
import sys

sample_list = []
gene_list = []
g2s = dict()
for filename in os.listdir('.'):
    if( not filename.endswith('.t_freq') ):
        continue
    sample_name = filename.split('.')[0]
    sample_list.append(sample_name)
    sys.stderr.write('Read %s as Sample %s... '%(filename,sample_name))
    f = open(filename,'r')
    f.readline()
    for line in f:
        tokens = line.strip().split('\t')
        gene_id = tokens[0]
        gene_list.append(gene_id)
        if(not g2s.has_key(gene_id) ):
            g2s[gene_id] = dict()
        g2s[gene_id][sample_name] = int(tokens[1])
    sys.stderr.write('Done\n')

sample_list = sorted(sample_list)
gene_list = sorted(list(set(gene_list)))
print "ID\t%s"%('\t'.join(sample_list))
for tmp_g in gene_list:
    out_list = [tmp_g]
    for tmp_s in sample_list:
        if( g2s[tmp_g].has_key(tmp_s) ):
            out_list.append('%d'%g2s[tmp_g][tmp_s])
        else:
            out_list.append('0')
    print "\t".join(out_list)
