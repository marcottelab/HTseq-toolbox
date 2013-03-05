#!/usr/bin/python
import os
import sys

data_name = sys.argv[1]

cdna_plen = []
ncdna_plen = []
cdna_nlen = []
ncdna_nlen = []
cdna_ratio = []
ncdna_ratio = []

cdna_st200_ratio = []
cdna_lt200_ratio = []
ncdna_lt200_ratio = []
ncdna_st200_ratio = []

f_cdna = open('%s.cdna_len_dist'%data_name,'r')
for line in f_cdna:
    tokens = line.strip().split("\t")
    tmp_nlen = int(tokens[1])
    cdna_nlen.append( tmp_nlen )
    cdna_plen.append( int(tokens[2]) )
    tmp_ratio = float(tokens[3]) 
    cdna_ratio.append( tmp_ratio )
    if( tmp_nlen < 200 ):
        cdna_st200_ratio.append(tmp_ratio)
    else:
        cdna_lt200_ratio.append(tmp_ratio)
f_cdna.close()

f_ncdna = open('%s.ncdna_len_dist'%data_name,'r')
for line in f_ncdna:
    tokens = line.strip().split("\t")
    tmp_nlen = int(tokens[1])
    ncdna_nlen.append( tmp_nlen ) 
    ncdna_plen.append( int(tokens[2]) )
    tmp_ratio = float(tokens[3]) 
    ncdna_ratio.append( tmp_ratio )
    if( tmp_nlen < 200 ):
        ncdna_st200_ratio.append(tmp_ratio)
    else:
        ncdna_lt200_ratio.append(tmp_ratio)
f_ncdna.close()

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fig = plt.figure(figsize=(11,8))

bins_n = range(0,10000,100)
bins_p = range(0,1000,10)

ax1 = fig.add_subplot(2,2,1)
ax1.set_position([0.05,0.55,0.40,0.40])
ax1.hist(ncdna_nlen,bins=bins_n,histtype='step',linewidth=2,edgecolor='black',normed=0,label='non-coding')
ax1.hist(cdna_nlen,bins=bins_n,histtype='step',linewidth=2,edgecolor='blue',normed=0,label='coding')
ax1.set_ylabel('Number of cdna sequences')
ax1.set_xlabel('cDNA length (bp)')
ax1.legend(prop=fm.FontProperties(size=11))
ax1.grid()
ax1.set_title(data_name)

ax2 = fig.add_subplot(2,2,2)
ax2.set_position([0.55,0.55,0.40,0.40])
ax2.hist(ncdna_plen,bins=bins_p,histtype='step',linewidth=2,edgecolor='black',normed=0,label='non-coding')
ax2.hist(cdna_plen,bins=bins_p,histtype='step',linewidth=2,edgecolor='blue',normed=0,label='coding')
ax2.set_ylabel('Number of protein sequences')
ax2.set_xlabel('Protein length (aa)')
ax2.legend(prop=fm.FontProperties(size=11))
ax2.grid()

ax3 = fig.add_subplot(2,2,3)
ax3.set_position([0.05,0.05,0.40,0.40])
ax3.hist(cdna_lt200_ratio,bins=100,histtype='step',lw=2,edgecolor='blue',normed=0,label='coding >= 100 bp')
ax3.hist(cdna_st200_ratio,bins=100,histtype='step',lw=2,edgecolor='cyan',normed=0,label='coding < 100 bp')
ax3.hist(ncdna_lt200_ratio,bins=100,histtype='step',lw=2,edgecolor='black',normed=0,label='non-coding >= 100 bp')
ax3.hist(ncdna_st200_ratio,bins=100,histtype='step',lw=2,edgecolor='grey',normed=0,label='non-coding < 100 bp')
ax3.set_ylabel('Number of sequences')
ax3.set_xlabel('Ratio of protein*3/cDNA length')
ax3.legend(prop=fm.FontProperties(size=11),loc='upper left')
ax3.grid()


plt.savefig('%s.len_dist.png'%data_name)
