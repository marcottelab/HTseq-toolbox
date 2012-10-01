#!/usr/bin/python
import os
import sys

filename_sum = sys.argv[1]

s_ratio_list = []
t1s_ratio_list = []
t1_ratio_list = []
t2_ratio_list = []
f_sum = open(filename_sum,'r')
for line in f_sum:
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    q_len = int(tokens[1])
    t1_id = tokens[2]
    t1_ratio = float(tokens[4])
    t2_id = tokens[8]
    t2_ratio = float(tokens[10])
    t1s_ratio_list.append(t1_ratio)
    if( t2_id == 'NA' ):
        s_ratio_list.append(t1_ratio)
    else:
        t1_ratio_list.append(t1_ratio)
        t2_ratio_list.append(t2_ratio)
f_sum.close()

#print "Single: ",len(t1_ratio_list) - len(t2_ratio_list)
for tmp_ratio in [x*0.01 for x in range(100,0,-1)]:
    t1s_count = len([x for x in t1s_ratio_list if x > tmp_ratio])
    t2_count = len([x for x in t2_ratio_list if x > tmp_ratio])
    if( t1s_count+t2_count == 0 ):
        continue
    tmp_t2_ratio = float(t2_count) / (t1s_count+t2_count)
    if( tmp_t2_ratio > 0.01 ):
        print tmp_ratio, tmp_t2_ratio, t1s_count, t2_count
        break

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(1,2,1)
n, bins, patches = ax1.hist(t1s_ratio_list,bins=100,edgecolor='none',label='1st+single')
ax1.hist(t1_ratio_list,bins=100,histtype='step',edgecolor='cyan',lw=2,label='1st')
ax1.hist(s_ratio_list,bins=100,histtype='step',edgecolor='orange',lw=2,label='single')
ax1.hist(t2_ratio_list,bins=100,histtype='step',edgecolor='black',lw=2,label='2nd')
ax1.set_xlim(0,1.01)
ax1.grid()
ax1.legend(loc='upper left', prop=fm.FontProperties(size=10))
ax1.set_xlabel('Align_len/Query_len ratio')
ax1.set_ylabel('Number of Query Sequences')
ax1.set_title('Overall')

ax2 = fig.add_subplot(1,2,2)
n, bins, patches = ax2.hist([x for x in t1s_ratio_list if x>0.8],bins=100,edgecolor='none',label='1st+single')
ax2.hist([x for x in t1_ratio_list if x>0.8],bins=100,histtype='step',edgecolor='cyan',lw=2,label='1st')
ax2.hist([x for x in s_ratio_list if x>0.8],bins=100,histtype='step',edgecolor='orange',lw=2,label='single')
ax2.hist([x for x in t2_ratio_list if x>0.8],bins=100,histtype='step',edgecolor='black',lw=2,label='2nd')
ax2.vlines(tmp_ratio, 0, max(n)*0.3, color='red',lw=3,label='1 pct cutoff (1st=%d;2nd=%d)'%(t1s_count,t2_count))
ax2.text(tmp_ratio, max(n)*0.3, '%.2f'%tmp_ratio, color='red')
ax2.set_xlim(0.8,1.001)
ax2.grid()
ax2.legend(loc='upper left', prop=fm.FontProperties(size=10))
ax2.set_xlabel('Align_len/Query_len ratio')
ax2.set_title('Zoom in: 0.80 ~ 1.00')

#plt.show()
plt.savefig('%s_dist.png'%filename_sum)
plt.savefig('%s_dist.pdf'%filename_sum)
