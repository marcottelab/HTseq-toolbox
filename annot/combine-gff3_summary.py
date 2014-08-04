#!/usr/bin/env python
import os
import sys
import gzip

#filename_out = 'XENTR_201407e.XENTR_JGIv80'
filename_out = sys.argv[1]

tx = dict()
tx_info = dict()
exon_len = dict()
for filename in os.listdir('.'):
    if( not filename.endswith('_summary.gz') ):
        continue

    sys.stderr.write('Read %s\n'%filename)
    f = gzip.open(filename,'r')
    for line in f:
        tokens = line.strip().split("\t")
        t_id = tokens[0]
        lib_id = tokens[1]
        seq_id = tokens[2]
        tmp_start = int(tokens[3])
        tmp_end = int(tokens[4])
        tmp_strand = tokens[5]
        tmp_cds_len = int(tokens[6])
        tmp_exon_len = int(tokens[7])
        tmp_exon_count = int(tokens[8])
        if( not tx.has_key(t_id) ):
            tx[t_id] = dict()
        if( not tx[t_id].has_key(tmp_cds_len) ):
            tx[t_id][tmp_cds_len] = []

        exon_len[seq_id] = tmp_exon_len
        tx_info[seq_id] = {'start':tmp_start, 'end':tmp_end, 'strand':tmp_strand, 'exon':tmp_exon_len, 'exon_count':tmp_exon_count}
        tx[t_id][tmp_cds_len].append(seq_id)
    f.close()

covered = dict()
f_log = open('%s.log'%filename_out,'w')
for t_id in sorted(tx.keys()):

    for tmp_cds_len in sorted(tx[t_id].keys(),reverse=True):
        for tmp_id in sorted(tx[t_id][tmp_cds_len],key=exon_len.get,reverse=False):
            tmp_start = tx_info[tmp_id]['start']
            tmp_end = tx_info[tmp_id]['end']
            tmp_strand = tx_info[tmp_id]['strand']
            tmp_cov_len = tmp_end - tmp_start
            tmp_exon_len = tx_info[tmp_id]['exon']
            tmp_exon_count = tx_info[tmp_id]['exon_count']

            is_covered = 0
            for tmp_cid in covered.keys():
                tmp_cstart = covered[tmp_cid]['start']
                tmp_cend = covered[tmp_cid]['end']
                tmp_cstrand = covered[tmp_cid]['strand']
                tmp_cov_exon_count = covered[tmp_cid]['exon_count']

                if( tmp_strand != tmp_cstrand ):
                    continue
                if( tmp_start >= tmp_cstart and tmp_end <= tmp_cend ):
                    is_covered = 1
                    break
                if( tmp_cstart >= tmp_start and tmp_cend <= tmp_end ):
                    is_covered = 1
                    break
               
                tmp_overlap_len = min([tmp_end, tmp_cend]) - max([tmp_start, tmp_cstart])
                if( tmp_cov_len - tmp_overlap_len < 1000 ):
                    is_covered = 1
                    break

            if( is_covered > 0 ):
                if( tmp_cov_exon_count >= tmp_exon_count ):
                    f_log.write("%s\t%s\t%d\t%d\t%s\t%d\t%d\t%s\t%d\t%d\n"%(t_id, tmp_id, tmp_start, tmp_end, tmp_strand, tmp_cds_len, tmp_exon_len, tmp_cid, tmp_cstart, tmp_cend))
                    continue
                else:
                    f_log.write("%s\t%s\t%d\t%d\t%s\t%d\t%d\t%s\t%d\t%d\treplace\n"%(t_id, tmp_id, tmp_start, tmp_end, tmp_strand, tmp_cds_len, tmp_exon_len, tmp_cid, tmp_cstart, tmp_cend))
                    del covered[tmp_cid]
                    out_str = "%s\t%s\t%d\t%d\t%s\t%d\t%d\t%d"%(t_id, tmp_id, tmp_start, tmp_end, tmp_strand, tmp_cds_len, tmp_exon_len, tmp_exon_count)
                    covered[tmp_id] = {'start': tmp_start, 'end':tmp_end, 'strand':tmp_strand, 'exon_count':tmp_exon_count, 'out_str':out_str }
            else:
                out_str = "%s\t%s\t%d\t%d\t%s\t%d\t%d\t%d"%(t_id, tmp_id, tmp_start, tmp_end, tmp_strand, tmp_cds_len, tmp_exon_len, tmp_exon_count)
                covered[tmp_id] = {'start': tmp_start, 'end':tmp_end, 'strand':tmp_strand, 'exon_count':tmp_exon_count, 'out_str':out_str }
f_log.close()

f_out = open('%s.out'%filename_out,'w')
for tmp_id in covered.keys():
    f_out.write('%s\n'%(covered[tmp_id]['out_str']))
f_out.close()
