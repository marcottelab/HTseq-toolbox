#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_gff = sys.argv[1]
filename_base = filename_gff

genes = dict()
gff = dict()
f_gff = open(filename_gff,'r')
if( filename_gff.endswith('.gz') ):
    f_gff = gzip.open(filename_gff,'rb')
    filename_base = re.sub(r'.gz$','',filename_gff)

for line in f_gff:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    t_id = tokens[0]
    tmp_type = tokens[2]
    tmp_start = int(tokens[3])
    tmp_end = int(tokens[4])
    tmp_strand = tokens[7]
    tmp_desc_tokens = tokens[8].split(';')

    tmp_mrna_id = 'NA'
    for tmp in tmp_desc_tokens:
        if( tmp_type == 'mRNA' ):
            if( tmp.startswith('ID=') ):
                tmp_mrna_id = tmp.replace('ID=','')
        elif( tmp_type == 'CDS' or tmp_type == 'exon' ):
            if( tmp.startswith('Parent=') ):
                tmp_mrna_id = tmp.replace('Parent=','')
    
    if( tmp_mrna_id == 'NA' or not tmp_mrna_id.endswith('1') ):
        continue
    
    if( not genes.has_key(tmp_mrna_id) ):
        genes[tmp_mrna_id] = {'t_id':t_id, 'start':tmp_start, 'end':tmp_end, 'exon':0, 'CDS':0}
        gff[tmp_mrna_id] = []

    if( tmp_type == 'exon' ):
        genes[tmp_mrna_id]['exon'] += (tmp_end - tmp_start)
        gff[tmp_mrna_id].append( line.strip() )
    elif( tmp_type == 'CDS' ):
        genes[tmp_mrna_id]['CDS'] += (tmp_end - tmp_start)
        gff[tmp_mrna_id].append( line.strip() )
    elif( tmp_type == 'mRNA' ):
        tokens[2] = 'gene'
        tokens[8] = '%s;%s'%(tmp_desc_tokens[0].replace('mrna','path'),tmp_desc_tokens[1])
        gff[tmp_mrna_id].append( '\t'.join(tokens) )
        gff[tmp_mrna_id].append( line.strip() )

f_gff.close()

target2cds = dict()
cds_len = dict()
exon_len = dict()
for tmp_id in genes.keys():
    tmp = genes[tmp_id]
    tmp_t_id = tmp['t_id']
    ## for assembled transcripts
    tmp_lib_name = tmp_id.split('_')[0]
    ## for other ref seqs
    #tmp_lib_name = filename_gff.split('.')[0]
    tmp_target_id = '%s\t%s'%(tmp_t_id, tmp_lib_name)
    
    if( not target2cds.has_key(tmp_target_id) ):
        target2cds[tmp_target_id] = dict()
    
    tmp_cds_len = tmp['CDS']
    if( not target2cds[tmp_target_id].has_key(tmp_cds_len) ):
        target2cds[tmp_target_id][tmp_cds_len] = []
    target2cds[tmp_target_id][tmp_cds_len].append( tmp_id )
    cds_len[tmp_id] = tmp_cds_len
    exon_len[tmp_id] = tmp['exon']

    #print "%s\t%s\t%d\t%d\t%d\t%d"%(tmp_id, tmp_t_id, tmp['start'], tmp['end'], tmp['exon'], tmp['CDS'])

f_out = open('%s_summary'%filename_base,'w')
f_log = open('%s_log'%filename_base,'w')
f_gff = open('%s_summary.gff3'%filename_base,'w')
f_gff.write('##gff-version 3\n')
for tmp_target_id in sorted(target2cds.keys()):
    covered = dict()
    for tmp_cds_len in sorted(target2cds[tmp_target_id].keys(),reverse=True):
        for tmp_id in sorted(target2cds[tmp_target_id][tmp_cds_len],key=exon_len.get,reverse=True):
            tmp_start = genes[tmp_id]['start']
            tmp_end = genes[tmp_id]['end']
            tmp_cov_len = tmp_end - tmp_start
            tmp_exon_len = genes[tmp_id]['exon']
            is_covered = 0
            for tmp_cid in covered.keys():
                tmp_cstart = covered[tmp_cid]['start']
                tmp_cend = covered[tmp_cid]['end']
                if( tmp_start >= tmp_cstart and tmp_end <= tmp_cend ):
                    is_covered = 1
                    break
               
                tmp_overlap_len = min([tmp_end, tmp_cend]) - max([tmp_start, tmp_cstart])
                if( tmp_cov_len - tmp_overlap_len < 1000 ):
                    is_covered = 1
                    break

            if( is_covered > 0 ):
                f_log.write("%s\t%s\t%d\t%d\t%d\t%d\t%s\t%d\t%d\n"%(tmp_target_id, tmp_id.replace('.mrna1',''), tmp_start, tmp_end, tmp_cds_len, tmp_exon_len,tmp_cid, tmp_cstart, tmp_cend))
                continue

            f_out.write("%s\t%s\t%d\t%d\t%d\t%d\n"%(tmp_target_id, tmp_id.replace('.mrna1',''), tmp_start, tmp_end, tmp_cds_len, tmp_exon_len))
            for tmp_line in gff[tmp_id]:
                f_gff.write('%s\n'%tmp_line)
            covered[tmp_id] = {'start': tmp_start, 'end':tmp_end}

f_log.close()
f_out.close()
f_gff.close()
