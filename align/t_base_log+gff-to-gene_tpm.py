#!/usr/bin/env python
import os
import sys
import gzip

filename_tblog = sys.argv[1]
filename_gff = sys.argv[2]

#filename_gff = '/work/PSEAE_net/genome/PSEAE_PA14_genome.gff3.gz'

pos2count = dict()
f_tblog = open(filename_tblog,'r')
if( filename_tblog.endswith('.gz') ):
    f_tblog = gzip.open(filename_tblog,'rb')
f_tblog.readline()
for line in f_tblog:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")

    t_id = tokens[0]
    tmp_pos = int(tokens[1])
    tmp_count_f = int(tokens[2])
    tmp_count_r = int(tokens[3])
    pos2count[tmp_pos] = {'+':tmp_count_f, '-':tmp_count_r}
f_tblog.close()

gene_counts = dict()
sum_T = 0
f_gff = open(filename_gff,'r')
if( filename_gff.endswith('.gz') ):
    f_gff = gzip.open(filename_gff,'rb')
for line in f_gff:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    tmp_type = tokens[2]
    tmp_start = int(tokens[3])
    tmp_end = int(tokens[4])
    tmp_strand = tokens[6]

    if( tmp_type != 'gene' ):
        continue

    ## This format may vary according to the source. 
    tmp_name = 'NA'
    tmp_id = 'NA'
    for tmp in tokens[8].split(';'):
        if( tmp.startswith('Alias=') ):
            tmp_id = tmp.split('=')[1]
        if( tmp.startswith('name=') ):
            tmp_name = tmp.split('=')[1]

    tmp_name_id = '%s|%s'%(tmp_id,tmp_name)
    if( tmp_name == tmp_id ):
        tmp_name_id = '%s|NA'%(tmp_id)
    if( tmp_id == 'NA' ):
        print "Error:",line.strip()
        sys.exit(1)

    count_f_list = []
    count_r_list = []
    for tmp_pos in range(tmp_start-1,tmp_end):
        count_f_list.append(pos2count[tmp_pos]['+'])
        count_r_list.append(pos2count[tmp_pos]['-'])

    tmp_len = tmp_end - tmp_start + 1
    mean_count_f = sum(count_f_list)*1.0/tmp_len
    mean_count_r = sum(count_r_list)*1.0/tmp_len
    gene_counts[tmp_name_id] = {'start':tmp_start, 'strand':tmp_strand, 'len':tmp_len, '+':mean_count_f, '-':mean_count_r}
    if( tmp_strand == '+' ):
        sum_T += mean_count_f
    else:
        sum_T += mean_count_r
f_gff.close()

print "#Gene\tLength\tPos\tStrand\tCount+\tCount-\tTPM"
print "#T_tpm = %.5f"%sum_T
tmp_sum = 0
for tmp_name_id in sorted(gene_counts.keys()):
    tmp = gene_counts[tmp_name_id]
    print "%s\t%d\t%d\t%s\t%.5f\t%.5f\t%.5f"%(tmp_name_id, tmp['len'], tmp['start'], tmp['strand'], tmp['+'], tmp['-'], tmp[tmp['strand']]*1000000.0/sum_T)
    tmp_sum += tmp[tmp['strand']]*1000000.0/sum_T
sys.stderr.write('SUM: %.3f\n'%tmp_sum)
