#!/usr/bin/env python
import os
import sys
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

dataset_name = sys.argv[1].strip()
genome_size = 4641652

pair_dist = dict()
for filename in os.listdir('.'):
    if( not filename.startswith(dataset_name) ):
        continue

    data_type = 'NA'
    if( filename.endswith('TG.txt') ):
        data_type = 'TG'
    elif( filename.endswith('TT.txt') ):
        data_type = 'TT'
    else:
        continue
    
    data_name = filename.split('.')[0]
    sample_name = '%s.%s'%(data_name, data_type)
    pair_dist[sample_name] = []

    sys.stderr.write('%s - %s\n'%(data_name, data_type))
    f = open(filename,'r')
    for line in f:
        tokens = line.strip().split("\t")
        pos_1 = int(tokens[1])
        seq_1 = tokens[2]
        pos_2 = int(tokens[3])
        seq_2 = tokens[4]
        tmp_dist = abs(pos_1 - pos_2)
        tmp_dist = min(tmp_dist, genome_size-tmp_dist)
        if( tmp_dist  < 10 ):
            continue

        tmp_dist = math.log10( tmp_dist )
        pair_dist[sample_name].append( tmp_dist )
    f.close()

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

for tmp_sample in sorted(pair_dist.keys()):
    if( tmp_sample.endswith('TG') ):
        ax1.hist(pair_dist[tmp_sample], bins=100, histtype='step', label=tmp_sample)
    if( tmp_sample.endswith('TT') ):
        ax2.hist(pair_dist[tmp_sample], bins=100, histtype='step', label=tmp_sample)

ax1.legend(loc='upper right', prop=fm.FontProperties(size=10))
ax2.legend(loc='upper right', prop=fm.FontProperties(size=10))
ax1.grid()
ax2.grid()
ax1.set_xlabel('Pair distance, log10(bp)')
ax1.set_ylabel('Frequnecy')
ax2.set_xlabel('Pair distance, log10(bp)')
ax2.set_ylabel('Frequnecy')
ax1.set_title('Tn-gDNA pairs')
ax2.set_title('Tn-Tn pairs')
plt.savefig('%s.pair_dist.png'%dataset_name)
