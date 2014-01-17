#!/usr/bin/python
import os
import sys

filename_top2 = sys.argv[1]

top2_list = []

s_ratio_list = []
t1_ratio_list = []
t1s_ratio_list = [] 
t2_ratio_list = []
f_top2 = open(filename_top2,'r')
for line in f_top2:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    top2_list.append(tokens)

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
f_top2.close()

count_total = len(top2_list)
sys.stderr.write('Total: %d, Single: %d (%.2f pct)\n'%(count_total, len(s_ratio_list), len(s_ratio_list)*100.0/count_total))

ratio_1pct = 0
ratio_5pct = 0
count_t1s_1pct = 0 
count_t2_1pct = 0
count_t1s_5pct = 0 
count_t2_5pct = 0

ratio_list = []
cum_t1_count = dict()
cum_s_count = dict()
cum_t2_count = dict()
for tmp_ratio in [x*0.01 for x in range(100,0,-1)]:
    ratio_list.append(tmp_ratio)
    t1_count = len([x for x in t1_ratio_list if x >= tmp_ratio])
    s_count = len([x for x in s_ratio_list if x >= tmp_ratio])
    t1s_count = t1_count + s_count
    t2_count = len([x for x in t2_ratio_list if x >= tmp_ratio])
    cum_t1_count[tmp_ratio] = t1_count
    cum_s_count[tmp_ratio] = s_count
    cum_t2_count[tmp_ratio] = t2_count

    if( t1s_count+t2_count == 0 ):
        continue
    tmp_t2_ratio = float(t2_count) / (t1s_count+t2_count)
    if( tmp_t2_ratio > 0.01 and ratio_1pct == 0 ):
        #sys.stderr.write('Test ratio:%.2f, T2 ratio:%.3f, T1 count:%d, T2 count:%d\n'%(tmp_ratio, tmp_t2_ratio, t1s_count, t2_count))
        ratio_1pct = tmp_ratio
        count_t1s_1pct = t1s_count
        count_t2_1pct = t2_count

    if( tmp_t2_ratio > 0.05 and ratio_5pct == 0 ):
        #sys.stderr.write('Test ratio:%.2f, T2 ratio:%.3f, T1 count:%d, T2 count:%d\n'%(tmp_ratio, tmp_t2_ratio, t1s_count, t2_count))
        ratio_5pct = tmp_ratio
        count_t1s_5pct = t1s_count
        count_t2_5pct = t2_count

sys.stderr.write('1 pct cutoff: %.2f (1st+single=%d;2nd=%d)\n'%(ratio_1pct,count_t1s_1pct,count_t2_1pct))
sys.stderr.write('5 pct cutoff: %.2f (1st+single=%d;2nd=%d)\n'%(ratio_5pct,count_t1s_5pct,count_t2_5pct))

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(1,2,1)
ax1.plot(ratio_list, [cum_t1_count[x]+cum_s_count[x] for x in ratio_list], markerfacecolor='blue', label='1st+single')
ax1.plot(ratio_list, [cum_t1_count[x] for x in ratio_list], markerfacecolor='cyan', label='1st')
ax1.plot(ratio_list, [cum_t2_count[x] for x in ratio_list], markerfacecolor='black', label='2nd')
ax1.plot(ratio_list, [cum_s_count[x] for x in ratio_list], markerfacecolor='lightgreen', label='single')
ax1.vlines(ratio_5pct, 0, count_total*0.5, color='red',lw=2,label='5 pct cutoff')
ax1.set_title('5pct cutoff=%.2f (1st+single=%d;2nd=%d)'%(ratio_5pct,count_t1s_5pct,count_t2_5pct))
ax1.invert_xaxis()
ax1.grid()
ax1.legend(loc='lower right', prop=fm.FontProperties(size=10))
ax1.set_xlabel('Align ratio')
ax1.set_ylabel('Cumulative Number of Query Sequences')

ax2 = fig.add_subplot(1,2,2)
ax2.plot(ratio_list, [(cum_t1_count[x]+cum_s_count[x])*1.0/count_total for x in ratio_list], markerfacecolor='blue', label='1st+single')
ax2.plot(ratio_list, [cum_t1_count[x]*1.0/count_total for x in ratio_list], markerfacecolor='cyan', label='1st')
ax2.plot(ratio_list, [cum_t2_count[x]*1.0/count_total for x in ratio_list], markerfacecolor='black', label='2nd')
ax2.plot(ratio_list, [cum_s_count[x]*1.0/count_total for x in ratio_list], markerfacecolor='lightgreen', label='single')
ax2.vlines(ratio_5pct, 0, 0.5, color='red',lw=2,label='5 pct cutoff')
ax2.invert_xaxis()
ax2.set_xlim(1.0, 0.5)
ax2.grid()
ax2.legend(loc='lower right', prop=fm.FontProperties(size=9))
ax2.set_xlabel('Align_ratio')
ax2.set_ylabel('Proportion of Query Seuqnces')

#plt.show()
plt.savefig('%s_dist.png'%filename_top2)
plt.savefig('%s_dist.pdf'%filename_top2)
