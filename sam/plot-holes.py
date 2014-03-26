#!/usr/bin/env python
import os
import sys

def read_holes(filename):
    rv = dict()
    f = open(filename,'r')
    for line in f:
        if( line.startswith('#') ):
            continue
        tokens = line.strip().split("\t")
        target_id = tokens[0]
        gap_start = int(tokens[1])
        gap_len = int(tokens[3])
        if( not rv.has_key(target_id) ):
            rv[ target_id ] = dict()
        rv[ target_id ][ gap_start ] = gap_len
    f.close()
    return rv

sample_list = ['QB928','LC8','LC33','HR23','MR3','TR7A','TR7B']

holes = dict()
holes100 = dict()

target_list = []
for filename in os.listdir('.'):
    if( filename.endswith('holes') ):
        sample_name = filename.split('_')[1]
        holes[sample_name] = read_holes(filename)
        target_list += list(set(holes[sample_name].keys()))
    elif( filename.endswith('holes100') ):
        sample_name = filename.split('_')[1]
        holes100[sample_name] = read_holes(filename)

target_list = list(set(target_list))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

for target_id in target_list:
    fig = plt.figure(figsize=(12,5))
    ax1 = fig.add_subplot(1,1,1)

    tmp_y = 0
    for tmp_sample in sample_list:
        holes_x = []
        holes100_x = []
        if( holes100[tmp_sample].has_key(target_id) ):
            for tmp_pos in holes100[tmp_sample][target_id]:
                holes100_x.append( (tmp_pos, holes100[tmp_sample][target_id][tmp_pos]) )
        if( holes[tmp_sample].has_key(target_id) ):
            for tmp_pos in holes[tmp_sample][target_id]:
                holes_x.append( (tmp_pos, holes[tmp_sample][target_id][tmp_pos]) )
    
        if( tmp_y == 0 ):
            ax1.broken_barh(holes_x, (tmp_y, 0.8), facecolor='black', edgecolor='black')
            ax1.broken_barh(holes100_x, (tmp_y, 0.8), facecolor='red', edgecolor='red')
        else:
            ax1.broken_barh(holes_x, (tmp_y, 0.8), facecolor='black', edgecolor='black')
            ax1.broken_barh(holes100_x, (tmp_y, 0.8), facecolor='red', edgecolor='red')

        tmp_y -= 1
    ax1.set_xlim(0,4500000)
    ax1.grid()
    ax1.set_yticks([x+0.4 for x in range(0,tmp_y,-1)])
    ax1.set_ylim(tmp_y+0.5,1)
    ax1.set_yticklabels(sample_list)
    ax1.set_title(target_id)
    plt.savefig('%s.holes.png'%target_id.replace('|','_'))
    plt.savefig('%s.holes.pdf'%target_id.replace('|','_'))
