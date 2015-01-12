#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_sam = sys.argv[1]
if( not filename_sam.endswith('_best') and not filename_sam.endswith('_best.gz') ):
    sys.stderr.write('Run sam-to-sam_best.py first. Exit.\n')
    sys.exit(1)

filename_base = re.sub(r'.sam_[A-z_]+_best[.gz]*','',filename_sam)
## ref: http://sqt.googlecode.com/git-history/hashing/sqt/cigar.py
def parse_cigar(tmp_cigar):
    rv = []
    n = ''
    count_M = 0
    for c in tmp_cigar:
        if c.isdigit():
            n += c
        else:
            rv.append( (c, int(n)) )
            if( c == 'M' ):
                count_M += 1
            n = ''
    
    start_pos = 0
    matched_len = 0
    if( count_M > 1 ):
        return start_pos, matched_len
    
    for tag,align_len in rv:
        if( tag == 'M' ):
            matched_len = align_len
            break
        if( tag == 'S' ):
            continue
        start_pos += align_len 
    return start_pos, matched_len

f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')

read_freq = dict()
hit_freq = dict()
for line in f_sam:
    if( line.startswith('@SQ') ):
        tokens = line.strip().split()
        seq_id = re.sub(r'^SN:','',tokens[1])
        hit_freq[seq_id] = [0 for x in range(0,int(re.sub(r'^LN:','',tokens[2])))]
        continue
    elif( len(line.split()[0]) < 5 ):
        continue

    tokens = line.strip().split("\t")
    read_id = tokens[0]
    pair_id = read_id.split('/')[0]
    tmp_flag = int(tokens[1])
    h1_t = tokens[2]
    h1_pos = int(tokens[3])
    tmp_mapq = int(tokens[4])
    tmp_cigar = tokens[5]
    h2_t = tokens[6]
    h2_pos = int(tokens[7])

    if( tmp_cigar == '*' or h1_t == '*' ):
        continue
    if( tmp_flag & 4 ):
        continue
    if( h1_pos == h2_pos ):
        continue

    if( not read_freq.has_key(h1_t) ):
        read_freq[h1_t] = 0
    read_freq[h1_t] += 1

    h1_start, h1_matched_len = parse_cigar(tmp_cigar)
    h1_start = h1_start + h1_pos - 1
    for tmp_pos in range(h1_start, h1_start+h1_matched_len):
        hit_freq[h1_t][tmp_pos] += 1
f_sam.close()

norm = dict()
sum_T = 0
sum_read_freq = sum(read_freq.values())
for tmp_id in hit_freq.keys():
    if( not read_freq.has_key(tmp_id) ):
        continue
    tmp_len = len(hit_freq[tmp_id])
    tmp_cov_len = tmp_len - hit_freq[tmp_id].count(0)
    if( tmp_cov_len == 0 ):
        continue

    tmp_count = sum(hit_freq[tmp_id])
    tmp_norm_count = sum(hit_freq[tmp_id])*1.0/tmp_len
    
    tmp_rpkm = read_freq[tmp_id] * 1000000.0 / sum_read_freq * 1000.0/tmp_len
    norm[tmp_id] = {'len':tmp_len, 'cov_len':tmp_cov_len, 'raw':tmp_count, 'norm':tmp_norm_count, 'rpkm':tmp_rpkm}
    sum_T += tmp_norm_count

f_out = open('%s.tpm'%filename_base,'w')
f_out.write('#SeqID\tSeqLen\tCovLenPct\tReadCount\tBaseCount\tRPKM\tTPM\n')
f_out.write('#Sum_T: %.5f\n#Sum_raw_count:%d\n'%(sum_T,sum_read_freq))
for tmp_id in sorted(norm.keys()):
    tmp_tpm = norm[tmp_id]['norm']*1000000.0/sum_T
    f_out.write('%s\t%d\t%.2f\t%d\t%d\t%.5f\t%.5f\n'%(tmp_id, norm[tmp_id]['len'], norm[tmp_id]['cov_len']*100.0/norm[tmp_id]['len'], read_freq[tmp_id], norm[tmp_id]['raw'], norm[tmp_id]['rpkm'], tmp_tpm))
f_out.close()
