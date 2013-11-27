#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_gff = sys.argv[1]
filename_base = filename_gff.replace('_gff','').replace('.gff','')

def read_gff(tmp_filename_gff):
    rv = dict()
    f_gff = open(tmp_filename_gff,'r')
    if( tmp_filename_gff.endswith('.gz') ):
        f_gff = gzip.open(tmp_filename_gff,'rb')

    for line in f_gff:
        if( line.startswith('#') ):
            continue

        tokens = line.strip().split("\t")
        tmp_t_id = tokens[0]
        tmp_type = tokens[2]
        tmp_t_start = int(tokens[3])
        tmp_t_end = int(tokens[4])
        tmp_desc_tokens = tokens[8].split(';')

        if( not rv.has_key(tmp_t_id) ):
            rv[tmp_t_id] = dict()
        
        if( tmp_type == 'gene' ):
            tmp_id = 'NA'
            for tmp in tmp_desc_tokens:
                if( tmp.startswith('ID=') ):
                    tmp_id = re.sub(r'^ID=','',tmp)
            if( tmp_id == 'NA' ):
                continue
            if( tmp_id.endswith('.path1') ):
                rv[tmp_t_id][tmp_id] = {'gene':line.strip(), 't_start':tmp_t_start, 't_end':tmp_t_end, 'mRNA':[], 'exon':[], 'CDS':[] }
        else:
            tmp_parent_id = 'NA'
            for tmp in tmp_desc_tokens:
                if( tmp.startswith('Parent') ):
                    tmp_parent_id = re.sub(r'^Parent=','',tmp).replace('.mrna','.path')
            
            if( tmp_parent_id == 'NA' ):
                continue
            if( not rv[tmp_t_id].has_key(tmp_parent_id) ):
                continue
            rv[tmp_t_id][tmp_parent_id][tmp_type].append( line.strip() )
    f_gff.close()
    return rv

def count_genes(tmp_gff):
    gene_list = []
    for tmp_tid in tmp_gff.keys():
        for tmp_gid in tmp_gff[tmp_tid].keys():
            gene_list.append(tmp_gid)
    return len(set(gene_list))

total_gene_count = dict()

gff = dict()
data_list = [filename_base]
if( not os.access(filename_gff, os.R_OK) ):
    sys.stderr.write('%s is not available.\n'%filename_gff)
    sys.exit(1)
gff[filename_base] = read_gff(filename_gff)
sys.stderr.write('%s -> %s: %d scaffolds, %d genes\n'%(filename_gff, filename_base,len(gff[filename_base]), count_genes(gff[filename_base])))

f_rep = open('%s_rep.gff'%filename_base,'w')
f_multi = open('%s_multi.gff'%filename_base,'w')
f_log = open('%s_log.gff'%filename_base,'w')

gene_tlen = dict()
gff_new = dict()
for tmp_data in data_list:
    for tmp_t_id in gff[tmp_data].keys():
        for tmp_g_id in gff[tmp_data][tmp_t_id].keys():
            tmp_t_start = gff[tmp_data][tmp_t_id][tmp_g_id]['t_start']
            tmp_t_end = gff[tmp_data][tmp_t_id][tmp_g_id]['t_end']
            tmp_t_range = tmp_t_end - tmp_t_start
            if( not gff_new.has_key(tmp_t_id) ):
                gff_new[tmp_t_id] = dict()
            if( not gff_new[tmp_t_id].has_key(tmp_t_range) ):
                gff_new[tmp_t_id][tmp_t_range] = dict()
            gff_new[tmp_t_id][tmp_t_range][tmp_g_id] = tmp_data
            gene_tlen[tmp_g_id] = tmp_t_range

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

for tmp_t_id in sorted(gff_new.keys()):
    query_list =  dict()
    sub_list = dict()
    border_list = dict()
    exclude_list = dict()

    tmp_t_range_list = sorted(gff_new[tmp_t_id].keys(),reverse=True)
    for i in range(0,len(tmp_t_range_list)):
        tmp_t_range_i = tmp_t_range_list[i]
        for tmp_gene_i in sorted(gff_new[tmp_t_id][tmp_t_range_i].keys(),key=gene_tlen.get,reverse=True):
            tmp_i = gff_new[tmp_t_id][tmp_t_range_i][tmp_gene_i]
            tmp_data_i = gff_new[tmp_t_id][tmp_t_range_i][tmp_gene_i]
            tmp_t_start_i = gff[tmp_data_i][tmp_t_id][tmp_gene_i]['t_start']
            tmp_t_end_i = gff[tmp_data_i][tmp_t_id][tmp_gene_i]['t_end']
            tmp_key_i = (tmp_data_i, tmp_gene_i)
            if( exclude_list.has_key(tmp_key_i) ):
                continue
            query_list[tmp_key_i] = tmp_t_start_i

            for j in range(i+1,len(tmp_t_range_list)):
                tmp_t_range_j = tmp_t_range_list[j]
                for tmp_gene_j in sorted(gff_new[tmp_t_id][tmp_t_range_j].keys(),key=gene_tlen.get,reverse=True):
                    tmp_j = gff_new[tmp_t_id][tmp_t_range_j][tmp_gene_j]
                    tmp_data_j = gff_new[tmp_t_id][tmp_t_range_j][tmp_gene_j]
                    tmp_t_start_j = gff[tmp_data_j][tmp_t_id][tmp_gene_j]['t_start']
                    tmp_t_end_j = gff[tmp_data_j][tmp_t_id][tmp_gene_j]['t_end']
                    
                    tmp_key_j = (tmp_data_j, tmp_gene_j)
                    if( exclude_list.has_key(tmp_key_j) ):
                        continue
                    if( tmp_t_start_j >= tmp_t_start_i and tmp_t_end_j <= tmp_t_end_i ):
                        if( not sub_list.has_key(tmp_key_i) ):
                            sub_list[tmp_key_i] = []
                        sub_list[tmp_key_i].append(tmp_key_j)
                        exclude_list[tmp_key_j] = 1

                    elif( (tmp_t_start_j <= tmp_t_end_i and tmp_t_end_j >= tmp_t_end_i) \
                        or (tmp_t_start_j <= tmp_t_start_i and tmp_t_end_j >= tmp_t_start_i) ):
                        
                        tmp_span_range = max(tmp_t_end_i, tmp_t_end_j) - min(tmp_t_start_i, tmp_t_start_j)
                        tmp_overlap = tmp_t_range_i + tmp_t_range_j - tmp_span_range
                        #sys.stderr.write('rep: %d, border: %d, overlap: %d, diff: %d, ratio: %.2f\n'%(tmp_t_range_i, tmp_t_range_j, tmp_overlap, tmp_t_range_j-tmp_overlap, tmp_overlap*100.0/tmp_t_range_j))
                        tmp_diff = tmp_t_range_j - tmp_overlap
                        if( tmp_diff < 100  ):
                            ## If difference is less than 100 bp, it is considered as 'subseq', instead of 'border'
                            if( not sub_list.has_key(tmp_key_i) ):
                                sub_list[tmp_key_i] = []
                            sub_list[tmp_key_i].append(tmp_key_j)
                            exclude_list[tmp_key_j] = 1
                        else:
                            ## Report gene_border separately, but treat it as an independent gene.
                            if( not border_list.has_key(tmp_key_i) ):
                                border_list[tmp_key_i] = []
                            border_list[tmp_key_i].append(tmp_key_j)
                            #exclude_list[tmp_key_j] = 1

    for tmp_q_data, tmp_q_gene in sorted(query_list.keys()):
        tmp_key_q = (tmp_q_data, tmp_q_gene)
        tmp_t_start = query_list[tmp_key_q]

        count_sub = 0
        if( sub_list.has_key(tmp_key_q) ):
            sub_list[tmp_key_q] = list(set(sub_list[tmp_key_q]))
            count_sub = len(sub_list[tmp_key_q])
        count_border = 0
        if( border_list.has_key(tmp_key_q) ):
            border_list[tmp_key_q] = list(set(border_list[tmp_key_q]))
            count_border = len(border_list[tmp_key_q])
        count_exon = len(gff[tmp_q_data][tmp_t_id][tmp_q_gene]['exon'])

        if( not total_rep.has_key(tmp_q_data) ):
            total_rep[tmp_q_data] = 0
        total_rep[tmp_q_data] += 1

        tmp_gene_str = gff[tmp_q_data][tmp_t_id][tmp_q_gene]['gene']
        prev_gene_tokens = tmp_gene_str.split(';')
        if( prev_gene_tokens[-2].startswith('sub=') and prev_gene_tokens[-1].startswith('border=') ):
            count_sub += int(prev_gene_tokens[-2].split('=')[1])
            count_border += int(prev_gene_tokens[-1].split('=')[1])
            tmp_gene_str = '%s;sub=%d;border=%d'%(';'.join(prev_gene_tokens[:-3]),count_sub, count_border)
        else:
            tmp_gene_str = '%s;sub=%d;border=%d'%(tmp_gene_str, count_sub, count_border)

        tmp_gene_e_str = gff[tmp_q_data][tmp_t_id][tmp_q_gene]['gene']
        if( len(prev_gene_tokens) >= 4 and  prev_gene_tokens[-3].startswith('sub=') and prev_gene_tokens[-2].startswith('border=') and prev_gene_tokens[-1].startswith('exon=') ):
            count_sub += int(prev_gene_tokens[-3].split('=')[1])
            count_border += int(prev_gene_tokens[-2].split('=')[1])
            count_exon += int(prev_gene_tokens[-1].split('=')[1])
            tmp_gene_e_str = '%s;sub=%d;border=%d;exon=%d'%(';'.join(prev_gene_tokens[:-4]),count_sub, count_border,count_)
        else:
            tmp_gene_e_str = '%s;sub=%d;border=%d;exon=%d'%(tmp_gene_e_str,count_sub,count_border,count_exon)

        f_log.write('%s\n'%tmp_gene_e_str)
        f_rep.write('%s\n'%tmp_gene_str)
        print_detail(f_rep, gff[tmp_q_data][tmp_t_id][tmp_q_gene])
        
        if( count_sub > 0 ):
            if( not total_multi.has_key(tmp_q_data) ):
                total_multi[tmp_q_data] = 0
            total_multi[tmp_q_data] += 1
            f_multi.write('%s\n'%tmp_gene_str)
            print_detail(f_multi, gff[tmp_q_data][tmp_t_id][tmp_q_gene])
            
            if( sub_list.has_key(tmp_key_q) ):
                for tmp_s_data, tmp_s_gene in sorted(sub_list[tmp_key_q]):
                    if( not total_sub.has_key(tmp_s_data) ):
                        total_sub[tmp_s_data] = []
                    total_sub[tmp_s_data].append(tmp_s_gene)
                    tmp_tokens = gff[tmp_s_data][tmp_t_id][tmp_s_gene]['gene'].split("\t")
                    tmp_tokens[2] = 'gene_sub'
                    tmp_tokens[-1] += ';exon_count=%d'%(len(gff[tmp_s_data][tmp_t_id][tmp_s_gene]['exon']))
                    f_log.write('%s\n'%'\t'.join(tmp_tokens))

        if( count_border > 0 and border_list.has_key(tmp_key_q) ):
            for tmp_b_data, tmp_b_gene in sorted(border_list[tmp_key_q]):
                if( not total_border.has_key(tmp_b_data) ):
                    total_border[tmp_b_data] = []
                total_border[tmp_b_data].append(tmp_s_gene)
                tmp_tokens = gff[tmp_b_data][tmp_t_id][tmp_b_gene]['gene'].split("\t")
                tmp_tokens[2] = 'gene_border'
                tmp_tokens[-1] += ';exon_count=%d'%(len(gff[tmp_b_data][tmp_t_id][tmp_b_gene]['exon']))
                f_log.write('%s\n'%'\t'.join(tmp_tokens))
                #print_detail(f_log, gff[tmp_b_data][tmp_t_id][tmp_b_gene])

sum_total_rep = sum(total_rep.values())
sum_total_multi = sum(total_multi.values())
sum_total_sub = 0
sum_total_border = 0

for tmp_data in sorted(total_rep.keys(),key=total_rep.get,reverse=True):
    tmp_sub_count = len(list(set(total_sub[tmp_data])))
    tmp_border_count = len(list(set(total_border[tmp_data])))
    sys.stderr.write('#%s - Total: %d, Rep: %d (%.1f pct), Multi: %d (%.1f pct), Sub: %d (%.1f pct), Border: %d\n'%(tmp_data, total_gene_count[tmp_data], total_rep[tmp_data], total_rep[tmp_data]*100.0/total_gene_count[tmp_data], total_multi[tmp_data], total_multi[tmp_data]*100.0/total_gene_count[tmp_data], tmp_sub_count, tmp_sub_count*100.0/total_gene_count[tmp_data], tmp_border_count))
    f_log.write('#%s - Total: %d, Rep: %d (%.1f pct), Multi: %d (%.1f pct), Sub: %d (%.1f pct), Border: %d\n'%(tmp_data, total_gene_count[tmp_data], total_rep[tmp_data], total_rep[tmp_data]*100.0/total_gene_count[tmp_data], total_multi[tmp_data], total_multi[tmp_data]*100.0/total_gene_count[tmp_data], tmp_sub_count, tmp_sub_count*100.0/total_gene_count[tmp_data], tmp_border_count))
    sum_total_sub += tmp_sub_count
    sum_total_border += tmp_border_count

sys.stderr.write('#Rep: %d, Multi: %d (%.1f pct or Rep.)\n'%(sum_total_rep, sum_total_multi, sum_total_multi*100.0/sum_total_rep))
f_log.write('#Rep: %d, Multi: %d (%.1f pct of Rep.)\n'%(sum_total_rep, sum_total_multi, sum_total_multi*100.0/sum_total_rep))
sys.stderr.write('#Sub: %d, Border: %d\n'%(sum_total_sub, sum_total_border))
f_log.write('#Sub: %d, Border: %d\n'%(sum_total_sub, sum_total_border))

f_rep.close()
f_multi.close()
f_log.close()
