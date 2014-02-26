#!/usr/bin/env python
import os
import sys

dataset_name = sys.argv[1].strip()

ins_sites = dict()
pos2seq = dict()
sample_list = []
sample_freq = dict()

flank_seq = dict()
f = open('%s_flank.seq'%dataset_name,'r')
for line in f:
    if( line.startswith('>') ):
        continue
    tmp_seq = line.strip()
    flank_seq[tmp_seq] = 1
f.close()

def left_right(tmp_seq):
    (tmp_5, tmp_3) = tmp_seq.split('.')
    if( tmp_5 == tmp_5.upper() and flank_seq.has_key(tmp_3) ):
        return 'left'
    if( tmp_3 == tmp_3.upper() and flank_seq.has_key(tmp_5) ):
        return 'right'
    return 'unknown'

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
    sample_freq[sample_name] = 0
    sample_list.append(sample_name)

    sys.stderr.write('%s - %s\n'%(data_name, data_type))
    f = open(filename,'r')
    for line in f:
        tokens = line.strip().split("\t")
        pos_1 = int(tokens[1])
        seq_1 = tokens[2]
        pos_2 = int(tokens[3])
        seq_2 = tokens[4]
        if( abs(pos_1 - pos_2) < 10 ):
            continue

        if( seq_1.find('.') > 0 ):
            if( not ins_sites.has_key(pos_1) ):
                ins_sites[pos_1] = dict()
            if( not ins_sites[pos_1].has_key(sample_name) ):
                ins_sites[pos_1][sample_name] = {'right':0, 'left':0, 'unknown':0}
            ins_sites[pos_1][sample_name][left_right(seq_1)] += 1

            if( not pos2seq.has_key(pos_1) ):
                pos2seq[pos_1] = dict()
            if( not pos2seq[pos_1].has_key(seq_1) ):
                pos2seq[pos_1][seq_1] = 0
            pos2seq[pos_1][seq_1] += 1

        if( seq_2.find('.') > 0 ):
            if( not ins_sites.has_key(pos_2) ):
                ins_sites[pos_2] = dict()
            if( not ins_sites[pos_2].has_key(sample_name) ):
                ins_sites[pos_2][sample_name] = {'right':0, 'left':0, 'unknown':0}
            ins_sites[pos_2][sample_name][left_right(seq_2)] += 1
            
            if( not pos2seq.has_key(pos_2) ):
                pos2seq[pos_2] = dict()
            if( not pos2seq[pos_2].has_key(seq_2) ):
                pos2seq[pos_2][seq_2] = 0
            pos2seq[pos_2][seq_2] += 1
    f.close()

sample_list = sorted(sample_list)
count_total = 0
count_single = 0
count_lt10 = 0
count_gt100 = 0

sum_count_list = []
TT_count_list = []

f_out = open('%s.ins_sites.txt'%dataset_name,'w')
f_out.write("Pos\tCountSum\tCountTT\t%s\tRepSeq\n"%('\t'.join(sample_list)))
for tmp_pos in sorted(ins_sites.keys()):
    out_str = []
    seq_list = sorted(pos2seq[tmp_pos].keys(), key=pos2seq[tmp_pos].get,reverse=True)
    sum_count = 0
    TT_count = 0
    for tmp_sample in sample_list:
        if( ins_sites[tmp_pos].has_key(tmp_sample) ):
            out_str.append( '%d,%d'%(ins_sites[tmp_pos][tmp_sample]['left'], ins_sites[tmp_pos][tmp_sample]['right']) )
            sum_count += ins_sites[tmp_pos][tmp_sample]['left']
            sum_count += ins_sites[tmp_pos][tmp_sample]['right']
            sample_freq[tmp_sample] += ins_sites[tmp_pos][tmp_sample]['left']
            sample_freq[tmp_sample] += ins_sites[tmp_pos][tmp_sample]['right']
            if( tmp_sample.endswith('TT') ):
                TT_count += ins_sites[tmp_pos][tmp_sample]['left']
                TT_count += ins_sites[tmp_pos][tmp_sample]['right']
        else:
            out_str.append('0,0')
    if( sum_count == 0 ):
        continue
    f_out.write("%s\t%d\t%d\t%s\t%s\n"%(tmp_pos, sum_count, TT_count, '\t'.join(out_str), seq_list[0]))
    if( sum_count > 1 ):
        sum_count_list.append(min(sum_count,100))
    if( TT_count > 1 ):
        TT_count_list.append(min(TT_count,100))

    count_total += 1
    if( sum_count == 1 ):
        count_single += 1
    elif( sum_count < 10 ):
        count_lt10 += 1
    elif( sum_count > 100 ):
        count_gt100 += 1

pct_single = count_single*100.0/count_total
pct_lt10 = count_lt10*100.0/count_total
pct_gt100 = count_gt100*100.0/count_total
sys.stderr.write('#Total=%d, Single=%d (%.2f pct), 1<n<10=%d (%.2f pct), >100=%d (%.2f pct)\n'%(count_total, count_single, pct_single, count_lt10, pct_lt10, count_gt100, pct_gt100))
f_out.write('#Total=%d, Single=%d (%.2f pct), 1<n<10=%d (%.2f pct), >100=%d (%.2f pct)\n'%(count_total, count_single, pct_single, count_lt10, pct_lt10, count_gt100, pct_gt100))
freq_total = sum(sample_freq.values())
for tmp_sample in sample_list:
    f_out.write('#Total %s = %d (%.2f pct)\n'%(tmp_sample, sample_freq[tmp_sample], sample_freq[tmp_sample]*100.0/freq_total))
    sys.stderr.write('#Total %s = %d (%.2f pct)\n'%(tmp_sample, sample_freq[tmp_sample], sample_freq[tmp_sample]*100.0/freq_total))
f_out.close()
