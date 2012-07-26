#!/usr/bin/env python
import os
import sys

filename_psort = sys.argv[1]

t_id = ''
t2pairs = dict()
t_freq = dict()

filename_base = filename_psort.replace('_psort','')
f_pdist = open('%s_pdist'%filename_base,'w')
f_pdist.write('TargetID\tPairID\tR1.strand\tR1.pos\tR1.cigar\tR2.strand\tR2.pos\tR2.cigar\n')

f_psort = open(filename_psort,'r')
for line in f_psort:
    if( line.startswith('@') ):
        continue
    tokens = line.strip().split("\t")
    tmp_read_id = tokens[0]
    tmp_pair_id = tmp_read_id.replace('/1','').replace('/2','')
    tmp_t_id = tokens[2]

    if( not t_freq.has_key(tmp_t_id) ):
        t_freq[tmp_t_id] = {'perfect':0, 'total':0, 'paired':0, 'perfect_paired':0, 'single':0, 'multi':0}
    t_freq[tmp_t_id]['total'] += 1
    if( tokens[5] == 'MD:Z:101' ):
        t_freq[tmp_t_id]['perfect'] += 1
    
    if( t_id == tmp_t_id ):
        if( not t2pairs.has_key(tmp_pair_id) ):
            t2pairs[tmp_pair_id] = dict()
        t2pairs[tmp_pair_id][tmp_read_id] = tokens
    else:
        for t_pair_id in t2pairs.keys():
            t_pair_read_list = sorted(t2pairs[t_pair_id].keys())
            if( len(t_pair_read_list) == 2 ):
                t_freq[t_id]['paired'] += 2
                r1 = t2pairs[t_pair_id][t_pair_read_list[0]]
                r2 = t2pairs[t_pair_id][t_pair_read_list[1]]
                if( r1[5] == 'MD:Z:101' and r2[5] == 'MD:Z:101' ):
                    t_freq[t_id]['perfect_paired'] += 2
                f_pdist.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(t_id,t_pair_id,r1[1],r1[3],r1[5],r2[1],r2[3],r2[5]))
            elif( len(t_pair_read_list) == 1 ):
                t_freq[t_id]['single'] += 1
            else:
                t_freq[t_id]['multi'] += len(t_pair_read_list)

        t_id = tmp_t_id
        t2pairs = dict()
f_psort.close()            
f_pdist.close()

f_pfreq = open('%s_pfreq'%filename_base,'w')
f_pfreq.write('TargetID\tTotalFreq\tPerfectFreq\tPairedRC\tPerfectPairedRC\tSingleRC\tMultiRC\n')
for tmp_t in sorted(t_freq.keys()):
    f_pfreq.write('%s\t%d\t%d\t%d\t%d\t%d\t%d\n'%(tmp_t,t_freq[tmp_t]['total'],t_freq[tmp_t]['perfect'],t_freq[tmp_t]['paired'],t_freq[tmp_t]['perfect_paired'],t_freq[tmp_t]['single'],t_freq[tmp_t]['multi']))
f_pfreq.close()
