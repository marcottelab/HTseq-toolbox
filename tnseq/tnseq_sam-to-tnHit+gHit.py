#!/usr/bin/env python
import os
import sys
import gzip

filename_sam = sys.argv[1]
filename_tnHit = filename_sam + '_tnHit'
filename_gHit = filename_sam + '_gHit'

min_matched_len = 10
max_matched_len = 80

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
        start_pos += align_len 
    return start_pos, matched_len

count_total = 0
count_perfect = 0
count_min_matched = 0
count_max_matched = 0

f_sam = open(filename_sam,'r')
if( filename_sam.endswith('.gz') ):
    f_sam = gzip.open(filename_sam,'rb')
    filename_tnHit = filename_sam.replace('.gz','')+'_tnHit'
    filename_gHit = filename_sam.replace('.gz','')+'_gHit'

f_tnHit = open(filename_tnHit,'w')
f_gHit = open(filename_gHit,'w')
for line in f_sam:
    tokens = line.strip().split("\t")
    if( tokens[0].startswith('@') and len(tokens[0]) < 4 ):
        #f_out.write('%s\n'%line.strip())
        continue
    
    count_total += 1

    read_id = tokens[0]
    target_id = tokens[2]
    target_pos = int(tokens[3])
    read_seq = tokens[9]
    read_len = len(read_seq)
    hit_flag = int(tokens[1])
    tmp_strand = '+'
    if( hit_flag & 16 ):
        tmp_strand = '-'
    
    tmp_cigar = tokens[5]
    if( tmp_cigar == '100M' ):
        count_perfect += 1
        f_gHit.write('%s\t%s\t%d\t%d\t%s\n'%(read_id, tmp_strand, target_pos, target_pos+100, read_seq))
        continue

    start_pos, matched_len = parse_cigar(tmp_cigar)
    if( matched_len > max_matched_len ):
        count_min_matched += 1
        f_gHit.write('%s\t%s\t%d\t%d\t%s\n'%(read_id, tmp_strand, target_pos, target_pos+matched_len, read_seq))
        continue
    if( matched_len < min_matched_len ):
        count_max_matched += 1
        continue
    out_seq_list = []
    for i in range(1,read_len+1):
        if( i >= start_pos and i <= start_pos + matched_len - 1 ):
            out_seq_list.append( read_seq[i-1].upper() )
        else:
            out_seq_list.append( read_seq[i-1].lower() )
    f_tnHit.write('%s\t%s\t%d\t%d\t%s\n'%(read_id, tmp_strand, target_pos, target_pos+matched_len, ''.join(out_seq_list)))
    #f_out.write('%s\n'%line.strip())
f_sam.close()
f_tnHit.write('#Total=%d, Perfect=%d (%.2fpct)\n'%(count_total,count_perfect,count_perfect*100.0/count_total))
f_tnHit.write('#MinMatched=%d (%.2fpct), MaxMatched=%d (%.2fpct)\n'%(count_min_matched, count_min_matched*100.0/count_total, count_max_matched, count_max_matched*100.0/count_total))
f_tnHit.close()
f_gHit.close()
