#!/usr/bin/env python
import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

dataset_name = sys.argv[1]

flank5 = dict()
flank3 = dict()

for filename in os.listdir('.'):
    if( not filename.startswith(dataset_name) ):
        continue
    if( not filename.endswith('TG.txt') and not filename.endswith('TT.txt') ):
        continue

    sys.stderr.write('Read %s\n'%filename)
    f_rpt = open(filename,'r')
    for line in f_rpt:
        tokens = line.strip().split("\t")
        seq1_tokens = tokens[2].split('.')
        seq2_tokens = tokens[4].split('.')
        if( len(seq1_tokens) > 1 ):
            if( seq1_tokens[0] == seq1_tokens[0].lower() ):
                tmp_flank5 =seq1_tokens[0]
                if( not flank5.has_key(tmp_flank5) ):
                    flank5[tmp_flank5] = 0
                flank5[tmp_flank5] += 1
            elif( seq1_tokens[1] == seq1_tokens[1].lower() ):
                tmp_flank3 =seq1_tokens[1]
                if( not flank3.has_key(tmp_flank3) ):
                    flank3[tmp_flank3] = 0
                flank3[tmp_flank3] += 1
     
        if( len(seq2_tokens) > 1 ):
            if( seq2_tokens[0] == seq2_tokens[0].lower() ):
                tmp_flank5 =seq2_tokens[0]
                if( not flank5.has_key(tmp_flank5) ):
                    flank5[tmp_flank5] = 0
                flank5[tmp_flank5] += 1
            elif( seq2_tokens[1] == seq2_tokens[1].lower() ):
                tmp_flank3 =seq2_tokens[1]
                if( not flank3.has_key(tmp_flank3) ):
                    flank3[tmp_flank3] = 0
                flank3[tmp_flank3] += 1
    f_rpt.close()

flank5_list = sorted(flank5.keys(),key=flank5.get,reverse=True)
flank3_list = sorted(flank3.keys(),key=flank3.get,reverse=True)

flank5_cum = 0
flank5_cum_list = []
flank3_cum = 0
flank3_cum_list = []

rank = 1
f_fa = open('%s_flank.fa'%dataset_name,'w')
for tmp_seq in flank5_list:
    flank5_cum += flank5[tmp_seq]
    flank5_cum_list.append(flank5_cum)
    if( flank5[tmp_seq] > 100 ):
        f_fa.write(">flank5_%04d.%d\n%s\n"%(rank,flank5[tmp_seq],tmp_seq))
        rank += 1
rank = 1
for tmp_seq in flank3_list:
    flank3_cum += flank3[tmp_seq]
    flank3_cum_list.append(flank3_cum)
    if( flank3[tmp_seq] > 100 ):
        f_fa.write(">flank3_%04d.%d\n%s\n"%(rank,flank3[tmp_seq],tmp_seq))
        rank += 1
f_fa.close()

fig = plt.figure(figsize=(9,4))

ax1 = fig.add_subplot(1,2,1)
ax2 = ax1.twinx()
def update_ax2(ax1):
    y1,y2 = ax1.get_ylim()
    ax2.set_ylim(y1*100.0/flank5_cum, y2*100.0/flank5_cum)
    ax2.set_yticks(range(0,101,10))
    ax2.figure.canvas.draw()
ax1.callbacks.connect("ylim_changed", update_ax2)
ax1.plot(range(0,len(flank5_cum_list)), flank5_cum_list, 'r-')
ax1.bar([x+0.5 for x in range(0,len(flank5_list))], [flank5[x] for x in flank5_list], 0.8, facecolor='red')
ax1.grid()
ax1.set_xlabel('Rank of occurrance')
ax1.set_ylabel('Counts')
ax1.set_xlim(0,10)
ax1.set_xticks(range(1,11))
top10_pct = flank5_cum_list[9]*100.0/flank5_cum
ax1.set_title('Flank5 (NN.xx);top10=%.1f pct'%top10_pct)

ax3 = fig.add_subplot(1,2,2)
ax4 = ax3.twinx()
def update_ax4(ax3):
    y1,y2 = ax3.get_ylim()
    ax4.set_ylim(y1*100.0/flank3_cum, y2*100.0/flank3_cum)
    ax4.set_yticks(range(0,101,10))
    ax4.figure.canvas.draw()
ax3.callbacks.connect("ylim_changed", update_ax4)
ax3.plot(range(0,len(flank3_cum_list)), flank3_cum_list, 'b-')
ax3.bar([x+0.5 for x in range(0,len(flank3_list))], [flank3[x] for x in flank3_list], 0.8, facecolor='blue')
ax3.grid()
ax3.set_xlabel('Rank of occurrance')
ax4.set_ylabel('Cumulative frequency')
ax3.set_xlim(0,10)
ax3.set_xticks(range(1,11))
top10_pct = flank3_cum_list[8]*100.0/flank3_cum
ax3.set_title('Flank3 (xx.NN);top9=%.1f pct'%top10_pct)
ax3.set_yticklabels([])

plt.savefig('%s_flank_freq.png'%dataset_name)
