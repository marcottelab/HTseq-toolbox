#!/usr/bin/env python
import os
import sys

filename_sam = sys.argv[1]
filename_out = filename_sam + '_tnHit'

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

f_out = open(filename_out,'w')
f_sam = open(filename_sam,'r')
for line in f_sam:
    tokens = line.strip().split("\t")
    if( tokens[0].startswith('@') and len(tokens[0]) < 4 ):
        #f_out.write('%s\n'%line.strip())
        continue
    
    tmp_cigar = tokens[5]
    if( tmp_cigar == '100M' ):
        continue
    read_id = tokens[0]
    target_id = tokens[2]
    target_pos = int(tokens[3])
    read_seq = tokens[9]
    read_len = len(read_seq)
    hit_flag = int(tokens[1])
    tmp_strand = '+'
    if( hit_flag & 16 ):
        tmp_strand = '-'

    start_pos, matched_len = parse_cigar(tmp_cigar)
    if( matched_len > read_len * 0.6 ):
        continue
    if( matched_len < read_len * 0.1 ):
        continue
    out_seq_list = []
    for i in range(1,read_len+1):
        if( i >= start_pos and i <= start_pos + matched_len - 1 ):
            out_seq_list.append( read_seq[i-1].upper() )
        else:
            out_seq_list.append( read_seq[i-1].lower() )
    f_out.write('%s\t%s\t%d\t%d\t%s\n'%(read_id, tmp_strand, target_pos, target_pos+matched_len, ''.join(out_seq_list)))
    #f_out.write('%s\n'%line.strip())
f_sam.close()
f_out.close()
