#!/usr/bin/python
import os
import sys

filename_pc = sys.argv[1]
data_name = filename_pc.replace('.pos_call','')

pos_map = dict()
f_pc = open(filename_pc,'r')
headers = f_pc.readline().strip().split("\t")
for line in f_pc:
    tokens = line.strip().split("\t")
    tmp_pos = int(tokens[0])
    pos_map[tmp_pos] = dict()
    for i in range(1,len(tokens)):
        pos_map[tmp_pos][headers[i]] = int(tokens[i])
f_pc.close()

n_list = sorted(headers[1:])
if( 'N' in n_list ):
    n_list.pop(n_list.index('N'))
    n_list.append('N')

pos_list = []
call_list = dict()
for tmp_n in n_list:
    call_list[tmp_n] = []

total_reads = sum(pos_map[0].values())
for tmp_pos in sorted(pos_map.keys()):
    pos_list.append(tmp_pos)
    tmp_count = 0
    for tmp_n in n_list:
        tmp_count += pos_map[tmp_pos][tmp_n]
        call_list[tmp_n].append(float(tmp_count)/total_reads)

n_colors = {'A':'green','C':'blue','G':'orange','T':'red','N':'grey'}

## http://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators-in-python-2-x
def num_group(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fig = plt.figure(figsize=(11,6))
ax1 = fig.add_subplot(1,1,1)
for tmp_n in n_list[::-1]:
    ax1.bar(pos_list,call_list[tmp_n],width=0.8,facecolor=n_colors[tmp_n],label=tmp_n)
ax1.set_xlabel('Position (bp)')
ax1.set_ylabel('Proportion of base calls')
ax1.set_xlim(0,max(pos_list)+1)
ax1.set_xticks(range(0,max(pos_list)+1,5))
ax1.set_yticks([0,0.25,0.50,0.75,1.0])
ax1.set_title('%s (read_count=%s)'%(data_name,num_group(total_reads)))
ax1.legend(loc='upper center',ncol=5,prop=fm.FontProperties(size=9))
ax1.grid()
#plt.show()
plt.savefig('%s.pos_call.png'%data_name)
