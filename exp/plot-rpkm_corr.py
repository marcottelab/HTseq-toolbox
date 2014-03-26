#!/usr/bin/env python
import os
import sys
import scipy.stats as stats
import math
import matplotlib.pyplot as plt

filename_file_list = sys.argv[1]
filename_corr_list = sys.argv[2]
filename_base = filename_file_list.split('.')[0]

def log10(tmp):
    if( tmp == 0.0 ):
        return -1 
    return math.log10(tmp)

group_list = []
gene_list = []
g2s = dict()
g2g = dict()
f_list = open(filename_file_list,'r')
for line in f_list:
    tokens = line.strip().split()
    sample_name = tokens[0]
    filename = tokens[1]
    if( not os.access(filename,os.R_OK) ):
        sys.stderr.write('%s is not available. Skip.\n'%filename)
        continue

    group_name = '_'.join(sample_name.split('_')[:-1])
    group_list.append(group_name)

    sys.stderr.write('Read %s as Sample %s... '%(filename,sample_name))
    f = open(filename,'r')
    f.readline()
    for line in f:
        if( line.startswith('#') ):
            continue
        tokens = line.strip().split('\t')
        gene_id = tokens[0]
        if(not g2s.has_key(gene_id) ):
            g2s[gene_id] = dict()
            g2g[gene_id] = dict()
            gene_list.append(gene_id)
        if(not g2g[gene_id].has_key(group_name)):
            g2g[gene_id][group_name] = []
        g2s[gene_id][sample_name] = float(tokens[1])
        g2g[gene_id][group_name].append( float(tokens[1]) ) 
    sys.stderr.write(' Done\n')

f_corr = open(filename_corr_list,'r')
for line in f_corr:
    tokens = line.strip().split()
    sample1 = tokens[0]
    sample2 = tokens[1]

    rpkm1 = []
    rpkm2 = []
    for gene_id in gene_list:
        if( not g2s[gene_id].has_key(sample1) and not g2s[gene_id].has_key(sample2) ):
            continue

        if( g2s[gene_id].has_key(sample1) ):
            rpkm1.append( log10(g2s[gene_id][sample1]) )
        else:
            rpkm1.append(-2.0)
        
        if( g2s[gene_id].has_key(sample2) ):
            rpkm2.append( log10(g2s[gene_id][sample2]) )
        else:
            rpkm2.append(-2.0)

    SpR, SpP= stats.spearmanr(rpkm1, rpkm2)

    fig = plt.figure(figsize=(12,5))
    ax1 = fig.add_subplot(1,2,1)
    ax1.plot(rpkm1, rpkm2,'k.')
    ax1.grid()
    ax1.set_xlabel(sample1)
    ax1.set_ylabel(sample2)
    ax1.set_title('SpR=%.2f, SpP=%.2f'%(SpR, SpP))
    
    ax2 = fig.add_subplot(1,2,2)
    ax2.hist(rpkm1, bins=100, histtype='step', label=sample1)
    ax2.hist(rpkm2, bins=100, histtype='step', label=sample2)
    ax2.grid()
    ax2.legend()
    ax2.set_xlabel(sample1)
    ax2.set_ylabel(sample2)
    ax2.set_ylim(0,2500)
    
    filename_png = '%s.%s-%s.png'%(filename_base,sample1,sample2)
    sys.stderr.write('Write %s\n'%filename_png)
    plt.savefig(filename_png)
f_corr.close()

group_list = sorted(list(set(group_list)))
for i in range(0,len(group_list)):
    group1 = group_list[i]
    for j in range(i+1,len(group_list)):
        group2 = group_list[j]

        rpkm1 = []
        rpkm2 = []
        for gene_id in gene_list:
            if( not g2g[gene_id].has_key(group1) and not g2g[gene_id].has_key(group2) ):
                continue

            if( g2g[gene_id].has_key(group1) ):
                rpkm1.append( log10( sum(g2g[gene_id][group1])*1.0/len(g2g[gene_id][group1])) )
            else:
                rpkm1.append(-2.0)
            
            if( g2g[gene_id].has_key(group2) ):
                rpkm2.append( log10( sum(g2g[gene_id][group2])*1.0/len(g2g[gene_id][group2])) )
            else:
                rpkm2.append(-2.0)
    
        SpR, SpP= stats.spearmanr(rpkm1, rpkm2)

        fig = plt.figure(figsize=(12,5))
        ax1 = fig.add_subplot(1,2,1)
        ax1.plot(rpkm1, rpkm2,'k.')
        ax1.grid()
        ax1.set_xlabel(group1)
        ax1.set_ylabel(group2)
        ax1.set_title('SpR=%.2f, SpP=%.2f'%(SpR, SpP))
        
        ax2 = fig.add_subplot(1,2,2)
        ax2.hist(rpkm1, bins=100, histtype='step', label=group1)
        ax2.hist(rpkm2, bins=100, histtype='step', label=group2)
        ax2.grid()
        ax2.legend()
        ax2.set_xlabel(group1)
        ax2.set_ylabel(group2)
        ax2.set_ylim(0,2500)
        
        filename_png = '%s.%s-%s.png'%(filename_base,group1,group2)
        sys.stderr.write('Write %s\n'%filename_png)
        plt.savefig(filename_png)
