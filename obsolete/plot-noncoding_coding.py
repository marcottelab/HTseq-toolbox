#!/usr/bin/python
import os
import sys

same_gene_list = []
diff_gene_list = []

filename_best = sys.argv[1]

part_list = dict()
f_part = open(filename_best.replace('_best','_part'),'r')
for line in f_part:
    tokens = line.strip().split("\t")
    part_list[tokens[0]] = tokens[2]
f_part.close()

f_best = open(filename_best,'r')
for line in f_best:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    q_len = int(tokens[1])
    t_id = tokens[2]
    t_len = int(tokens[3])
    align_len = int(tokens[4])
    mismatches = int(tokens[5])
    gap_open = int(tokens[6])

    if( part_list.has_key(q_id) ):
        continue

    if( q_id == t_id ):
        continue
    if( gap_open > 0 ):
        continue

    q_gene = q_id.split('|')[1]
    t_gene = t_id.split('|')[1]
    align_ratio = (align_len-mismatches)*100.0/q_len
    if( q_gene == t_gene ):
        same_gene_list.append( align_ratio )
    else:
        if( align_ratio > 95 ):
            print line.strip()
        diff_gene_list.append( align_ratio )
f_best.close()

#import matplotlib
#matplotlib.use('Agg')

sum_same_gene = sum(same_gene_list)
sum_diff_gene = sum(diff_gene_list)

cum_same = 0
cum_diff = 0
same_ratio = 0
cutoff_align_ratio = 0
for i in range(2,101):
    print i,same_ratio
    if( same_ratio > 0.05):
        break
    cum_same = sum([x for x in same_gene_list if x <= i])*1.0/sum_same_gene
    cum_diff = sum([x for x in diff_gene_list if x <= i])*1.0/sum_diff_gene
    if( cum_diff == 0 ):
        continue
    same_ratio = cum_same/cum_diff
    cutoff_align_ratio = i

sys.stderr.write('Cutoff ratio:%d (%.2f)\n'%(cutoff_align_ratio,same_ratio))

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(9,9))
ax1= fig.add_subplot(1,1,1)
ax1.hist(same_gene_list, bins=100, label='same (%d)'%len(same_gene_list), histtype='step', normed=True)
ax1.hist(diff_gene_list, bins=100, label='diff (%d)'%len(diff_gene_list), histtype='step', normed=True)
ax1.vlines(cutoff_align_ratio, 0, 0.02, color='r', label='5pct cutoff=%.2f'%cutoff_align_ratio)
ax1.grid()
ax1.legend(loc='upper center')
ax1.set_ylim(0,0.03)
ax1.set_xlabel('BLAST_align_ratio')
ax1.set_ylabel('Normalized frequency')
plt.savefig('%s.png'%filename_best)
#plt.show()
#Qid	QLen	Tid	TLen	AlignLen	Mismatches	GapOpens	BitScore
#0610007C21RIK|ENSMUSG00000013622|ENSMUST00000133215|non-coding	550	0610007C21RIK|ENSMUSG00000013622|ENSMUST00000013766|coding	976	464	0	0	857
