#!/usr/bin/env python
import os
import sys
import re
import gzip
import gff_parser

filename_gff = sys.argv[1]
filename_top2 = sys.argv[2]

filename_base = filename_gff.replace('_gff','').replace('.gff','')

total_gene_count = dict()

gff = dict()
data_list = [filename_base]
if( not os.access(filename_gff, os.R_OK) ):
    sys.stderr.write('%s is not available.\n'%filename_gff)
    sys.exit(1)
gff[filename_base] = gff_parser.read_gmap_gff(filename_gff)

count_scaffolds = len(gff[filename_base].keys())
count_genes = gff_parser.count_genes(gff[filename_base])
total_gene_count[filename_base] = count_genes
sys.stderr.write('%s -> %s: %d scaffolds, %d genes\n'%(filename_gff, filename_base, count_scaffolds, count_genes))

best_cov_gff = dict()
best_cov_gff[filename_base] = gff_parser.filter_top2(gff[filename_base],filename_top2)

f_rep = open('%s_rep.gff'%filename_base,'w')
f_multi = open('%s_multi.gff'%filename_base,'w')
f_log = open('%s_log.gff'%filename_base,'w')

gene2data = dict()
t_range_list = dict()
gff_new = dict()
for tmp_data in data_list:
    for tmp_t_id in best_cov_gff[tmp_data].keys():
        if( not t_range_list.has_key(tmp_t_id) ):
            t_range_list[tmp_t_id] = dict()
            gff_new[tmp_t_id] = dict()
        for tmp_g_id in best_cov_gff[tmp_data][tmp_t_id].keys():
            if( t_range_list[tmp_t_id].has_key(tmp_g_id) ):
                ## Duplicated query_id is not allowed here.
                sys.stderr.write('Duplicate: %s\n'%tmp_g_id)
                sys.exit(1)
            t_range_list[tmp_t_id][tmp_g_id] = best_cov_gff[tmp_data][tmp_t_id][tmp_g_id]['t_range']
            gff_new[tmp_t_id][tmp_g_id] = best_cov_gff[tmp_data][tmp_t_id][tmp_g_id]
            gene2data[tmp_g_id] = tmp_data

total_rep = dict()
total_multi = dict()
total_sub = dict()
total_border = dict()

def print_detail(fh, tmp_gff):
    for tmp_m in tmp_gff['mRNA']:
        fh.write('%s\n'%tmp_m)
    for tmp_e in tmp_gff['exon']:
        fh.write('%s\n'%tmp_e)
    for tmp_c in tmp_gff['CDS']:
        fh.write('%s\n'%tmp_c)

for tmp_t_id in sorted(t_range_list.keys()):
    query_list =  dict()
    sub_list = dict()
    border_list = dict()
    exclude_list = dict()

    tmp_g_list = sorted(t_range_list[tmp_t_id].keys(), key=t_range_list[tmp_t_id].get, reverse=True)
    tmp_g_list_len = len(tmp_g_list)

    for i in range(0,tmp_g_list_len):
        tmp_gene_i = tmp_g_list[i]
        tmp_t_range_i = t_range_list[tmp_t_id][tmp_gene_i]

        tmp_gff_i = gff_new[tmp_t_id][tmp_gene_i]
        tmp_t_start_i = tmp_gff_i['t_start']
        tmp_t_end_i = tmp_gff_i['t_end']
        tmp_strand_i = tmp_gff_i['strand']
        if( exclude_list.has_key(tmp_gene_i) ):
            continue
        query_list[tmp_gene_i] = tmp_t_start_i

        for j in range(i+1,tmp_g_list_len):
            tmp_gene_j = tmp_g_list[j]
            tmp_t_range_j = t_range_list[tmp_t_id][tmp_gene_j]

            tmp_gff_j = gff_new[tmp_t_id][tmp_gene_j]
            tmp_t_start_j = tmp_gff_j['t_start']
            tmp_t_end_j = tmp_gff_j['t_end']
            tmp_strand_j = tmp_gff_j['strand']
                
            if( exclude_list.has_key(tmp_gene_j) ):
                continue

            if( tmp_t_start_j >= tmp_t_start_i and tmp_t_end_j <= tmp_t_end_i and tmp_strand_i == tmp_strand_j ):
                ### t_start_i < t_start_j < t_end_j < t_end_i : complete subset
                if( not sub_list.has_key(tmp_gene_i) ):
                    sub_list[tmp_gene_i] = []
                sub_list[tmp_gene_i].append(tmp_gene_j)
                exclude_list[tmp_gene_j] = 1

            elif( (tmp_t_start_j <= tmp_t_end_i and tmp_t_end_j >= tmp_t_end_i and tmp_strand_i == tmp_strand_j ) \
                or (tmp_t_start_j <= tmp_t_start_i and tmp_t_end_j >= tmp_t_start_i and tmp_strand_i == tmp_strand_j ) ):
                
                tmp_span_range = max(tmp_t_end_i, tmp_t_end_j) - min(tmp_t_start_i, tmp_t_start_j)
                tmp_overlap = tmp_t_range_i + tmp_t_range_j - tmp_span_range
                #sys.stderr.write('rep: %d, border: %d, overlap: %d, diff: %d, ratio: %.2f\n'%(tmp_t_range_i, tmp_t_range_j, tmp_overlap, tmp_t_range_j-tmp_overlap, tmp_overlap*100.0/tmp_t_range_j))
                tmp_diff = tmp_t_range_j - tmp_overlap
                if( tmp_diff < 100  ):
                    ## If difference is less than 100 bp, it is considered as 'subseq', instead of 'border'
                    if( not sub_list.has_key(tmp_gene_i) ):
                        sub_list[tmp_gene_i] = []
                    sub_list[tmp_gene_i].append(tmp_gene_j)
                    exclude_list[tmp_gene_j] = 1
                else:
                    ## Report gene_border separately, but treat it as an independent gene.
                    if( not border_list.has_key(tmp_gene_i) ):
                        border_list[tmp_gene_i] = []
                    border_list[tmp_gene_i].append(tmp_gene_j)
                    #exclude_list[tmp_key_j] = 1

    for tmp_q_id in sorted(query_list.keys()):
        tmp_q_data = gene2data[tmp_q_id ]
        tmp_t_start = query_list[tmp_q_id]

        count_sub = 0
        if( sub_list.has_key(tmp_q_id) ):
            sub_list[tmp_q_id] = list(set(sub_list[tmp_q_id]))
            count_sub = len(sub_list[tmp_q_id])
        count_border = 0
        if( border_list.has_key(tmp_q_id) ):
            border_list[tmp_q_id] = list(set(border_list[tmp_q_id]))
            count_border = len(border_list[tmp_q_id])
        count_exon = len(gff[tmp_q_data][tmp_t_id][tmp_q_id]['exon'])

        if( not total_rep.has_key(tmp_q_data) ):
            total_rep[tmp_q_data] = 0
        total_rep[tmp_q_data] += 1

        tmp_gene_str = best_cov_gff[tmp_q_data][tmp_t_id][tmp_q_id]['gene']
        prev_gene_tokens = tmp_gene_str.split(';')
        if( prev_gene_tokens[-2].startswith('sub=') and prev_gene_tokens[-1].startswith('border=') ):
            count_sub += int(prev_gene_tokens[-2].split('=')[1])
            count_border += int(prev_gene_tokens[-1].split('=')[1])
            tmp_gene_str = '%s;sub=%d;border=%d'%(';'.join(prev_gene_tokens[:-3]),count_sub, count_border)
        else:
            tmp_gene_str = '%s;sub=%d;border=%d'%(tmp_gene_str, count_sub, count_border)

        tmp_gene_e_str = best_cov_gff[tmp_q_data][tmp_t_id][tmp_q_id]['gene']
        if( len(prev_gene_tokens) >= 4 and  prev_gene_tokens[-3].startswith('sub=') and prev_gene_tokens[-2].startswith('border=') and prev_gene_tokens[-1].startswith('exon=') ):
            count_sub += int(prev_gene_tokens[-3].split('=')[1])
            count_border += int(prev_gene_tokens[-2].split('=')[1])
            count_exon = max(count_exon, int(prev_gene_tokens[-1].split('=')[1]))
            tmp_gene_e_str = '%s;sub=%d;border=%d;exon=%d'%(';'.join(prev_gene_tokens[:-4]),count_sub, count_border,count_)
        else:
            tmp_gene_e_str = '%s;sub=%d;border=%d;exon=%d'%(tmp_gene_e_str,count_sub,count_border,count_exon)

        f_log.write('%s\n'%tmp_gene_e_str)
        f_rep.write('%s\n'%tmp_gene_str)
        print_detail(f_rep, best_cov_gff[tmp_q_data][tmp_t_id][tmp_q_id])
        
        if( count_sub > 0 ):
            if( not total_multi.has_key(tmp_q_data) ):
                total_multi[tmp_q_data] = 0
            total_multi[tmp_q_data] += 1
            f_multi.write('%s\n'%tmp_gene_str)
            print_detail(f_multi, gff_new[tmp_t_id][tmp_q_id])
            
            if( sub_list.has_key(tmp_q_id) ):
                for tmp_s_id in sorted(sub_list[tmp_q_id]):
                    tmp_s_data = gene2data[tmp_s_id]
                    if( not total_sub.has_key(tmp_s_data) ):
                        total_sub[tmp_s_data] = []
                    total_sub[tmp_s_data].append(tmp_s_id)
                    tmp_tokens = gff_new[tmp_t_id][tmp_s_id]['gene'].split("\t")
                    tmp_tokens[2] = 'gene_sub'
                    tmp_tokens[-1] += ';exon_count=%d'%(len(gff_new[tmp_t_id][tmp_s_id]['exon']))
                    f_log.write('%s\n'%'\t'.join(tmp_tokens))

        if( count_border > 0 and border_list.has_key(tmp_q_id) ):
            for tmp_b_id in sorted(border_list[tmp_q_id]):
                tmp_b_data = gene2data[tmp_b_id]
                if( not total_border.has_key(tmp_b_data) ):
                    total_border[tmp_b_data] = []
                total_border[tmp_b_data].append(tmp_b_id)
                tmp_tokens = gff_new[tmp_t_id][tmp_b_id]['gene'].split("\t")
                tmp_tokens[2] = 'gene_border'
                tmp_tokens[-1] += ';exon_count=%d'%(len(gff_new[tmp_t_id][tmp_b_id]['exon']))
                f_log.write('%s\n'%'\t'.join(tmp_tokens))
                #print_detail(f_log, gff[tmp_b_data][tmp_t_id][tmp_b_gene])

sum_total_rep = sum(total_rep.values())
sum_total_multi = sum(total_multi.values())
sum_total_sub = 0
sum_total_border = 0

for tmp_data in sorted(total_rep.keys(),key=total_rep.get,reverse=True):
    tmp_sub_count = len(list(set(total_sub[tmp_data])))
    tmp_border_count = 0
    if( total_border.has_key(tmp_data) ):
        tmp_border_count = len(list(set(total_border[tmp_data])))
    tmp_total_count = total_gene_count[tmp_data]
    tmp_total_rep = total_rep[tmp_data]
    tmp_total_multi = total_multi[tmp_data]
    tmp_total_sub = total_multi[tmp_data]
    sys.stderr.write('#%s - Total: %d, Rep: %d (%.1f pct), Multi: %d (%.1f pct), Sub: %d (%.1f pct), Border: %d\n'%(tmp_data, tmp_total_count, tmp_total_rep, tmp_total_rep*100.0/tmp_total_count, tmp_total_multi, tmp_total_multi*100.0/tmp_total_count, tmp_sub_count, tmp_sub_count*100.0/tmp_total_count, tmp_border_count))
    f_log.write('#%s - Total: %d, Rep: %d (%.1f pct), Multi: %d (%.1f pct), Sub: %d (%.1f pct), Border: %d\n'%(tmp_data, tmp_total_count, tmp_total_rep, tmp_total_rep*100.0/tmp_total_count, tmp_total_multi, tmp_total_multi*100.0/tmp_total_count, tmp_sub_count, tmp_sub_count*100.0/tmp_total_count, tmp_border_count))
    sum_total_sub += tmp_sub_count
    sum_total_border += tmp_border_count

sys.stderr.write('#Rep: %d, Multi: %d (%.1f pct or Rep.)\n'%(sum_total_rep, sum_total_multi, sum_total_multi*100.0/sum_total_rep))
f_log.write('#Rep: %d, Multi: %d (%.1f pct of Rep.)\n'%(sum_total_rep, sum_total_multi, sum_total_multi*100.0/sum_total_rep))
sys.stderr.write('#Sub: %d, Border: %d\n'%(sum_total_sub, sum_total_border))
f_log.write('#Sub: %d, Border: %d\n'%(sum_total_sub, sum_total_border))

f_rep.close()
f_multi.close()
f_log.close()
