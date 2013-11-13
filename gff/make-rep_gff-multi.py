#!/usr/bin/env python
import os
import sys
import re
import gzip

filename_list = sys.argv[1]
filename_base = filename_list.split('.')[0]

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

gff = dict()
data_list = []
f_list = open(filename_list,'r')
for line in f_list:
    (tmp_dataname, tmp_filename) = line.strip().split()
    if( not os.access(tmp_filename, os.R_OK) ):
        sys.stderr.write('%s is not available.\n'%tmp_filename)
        continue
    gff[tmp_dataname] = read_gff(tmp_filename)
    data_list.append(tmp_dataname)
    sys.stderr.write('%s -> %s: %d scaffolds, %d genes\n'%(tmp_filename, tmp_dataname,len(gff[tmp_dataname]), count_genes(gff[tmp_dataname])))
f_list.close()

f_rep = open('%s_rep.gff'%filename_base,'w')
f_multi = open('%s_multi.gff'%filename_base,'w')
f_full = open('%s_full_gene.gff'%filename_base,'w')

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
            gene_tlen[tmp_g_id] = tmp_t_end - tmp_t_start

total_rep = dict()
total_multi = dict()
total_sub = 0
total_border = 0

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

                    if( tmp_t_start_j >= tmp_t_start_i and tmp_t_end_j <= tmp_t_end_i ):
                        tmp_key_j = (tmp_data_j, tmp_gene_j)
                        if( not sub_list.has_key(tmp_key_i) ):
                            sub_list[tmp_key_i] = []
                        sub_list[tmp_key_i].append(tmp_key_j)
                        exclude_list[tmp_key_j] = 1

                    elif( (tmp_t_start_j <= tmp_t_end_i and tmp_t_end_j >= tmp_t_end_i) \
                        or (tmp_t_start_j <= tmp_t_start_i and tmp_t_end_j >= tmp_t_start_i) ):
                        tmp_key_j = (tmp_data_j, tmp_gene_j)
                        if( not border_list.has_key(tmp_key_i) ):
                            border_list[tmp_key_i] = []
                        border_list[tmp_key_i].append(tmp_key_j)
                        exclude_list[tmp_key_j] = 1

    for tmp_q_data, tmp_q_gene in sorted(query_list.keys()):
        tmp_key_q = (tmp_q_data, tmp_q_gene)
        tmp_t_start = query_list[tmp_key_q]

        count_sub = 0
        if( sub_list.has_key(tmp_key_q) ):
            count_sub = len(sub_list[tmp_key_q])
        count_border = 0
        if( border_list.has_key(tmp_key_q) ):
            count_border = len(border_list[tmp_key_q])
        count_exon = len(gff[tmp_q_data][tmp_t_id][tmp_q_gene]['exon'])

        if( not total_rep.has_key(tmp_q_data) ):
            total_rep[tmp_q_data] = 0
        total_rep[tmp_q_data] += 1

        f_rep.write('%s;sub=%d;border=%d\n'%(gff[tmp_q_data][tmp_t_id][tmp_q_gene]['gene'],count_sub,count_border))
        f_full.write('%s;sub=%d;border=%d;exon=%d\n'%(gff[tmp_q_data][tmp_t_id][tmp_q_gene]['gene'],count_sub,count_border,count_exon))
        print_detail(f_rep, gff[tmp_q_data][tmp_t_id][tmp_q_gene])
        
        if( count_sub > 0 ):
            if( not total_multi.has_key(tmp_q_data) ):
                total_multi[tmp_q_data] = 0
            total_multi[tmp_q_data] += 1
            f_multi.write('%s;sub=%d;border=%d\n'%(gff[tmp_q_data][tmp_t_id][tmp_q_gene]['gene'],count_sub,count_border))
            print_detail(f_multi, gff[tmp_q_data][tmp_t_id][tmp_q_gene])

            for tmp_s_data, tmp_s_gene in sorted(sub_list[tmp_key_q]):
                total_sub += 1
                tmp_tokens = gff[tmp_s_data][tmp_t_id][tmp_s_gene]['gene'].split("\t")
                tmp_tokens[2] = 'gene_sub'
                tmp_tokens[-1] += ';exon_count=%d'%(len(gff[tmp_s_data][tmp_t_id][tmp_s_gene]['exon']))
                f_full.write('%s\n'%'\t'.join(tmp_tokens))
                #print_detail(f_full, gff[tmp_s_data][tmp_t_id][tmp_s_gene])

        if( count_border > 0 ):
            for tmp_b_data, tmp_b_gene in sorted(border_list[tmp_key_q]):
                total_border += 1
                tmp_tokens = gff[tmp_b_data][tmp_t_id][tmp_b_gene]['gene'].split("\t")
                tmp_tokens[2] = 'gene_border'
                tmp_tokens[-1] += ';exon_count=%d'%(len(gff[tmp_b_data][tmp_t_id][tmp_b_gene]['exon']))
                f_full.write('%s\n'%'\t'.join(tmp_tokens))
                #print_detail(f_full, gff[tmp_b_data][tmp_t_id][tmp_b_gene])

sys.stderr.write('Rep: %d, Multi: %d\n'%(sum(total_rep.values()), sum(total_multi.values())))
f_full.write('#Rep: %d, Multi: %d\n'%(sum(total_rep.values()), sum(total_multi.values())))
for tmp_data in sorted(total_rep.keys(),key=total_rep.get,reverse=True):
    sys.stderr.write('%s - Rep: %d, Multi: %d\n'%(tmp_data, total_rep[tmp_data], total_multi[tmp_data]))
    f_full.write('#%s - Rep: %d, Multi: %d\n'%(tmp_data, total_rep[tmp_data], total_multi[tmp_data]))
sys.stderr.write('Sub: %d, Border: %d\n'%(total_sub, total_border))
f_full.write('#Sub: %d, Border: %d\n'%(total_sub, total_border))

f_rep.close()
f_multi.close()
f_full.close()
