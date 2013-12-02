import re
import gzip

def read_gmap_gff(tmp_filename_gff):
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
        tmp_strand = tokens[6]
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
            if( not rv[tmp_t_id].has_key( tmp_id ) ):
                rv[tmp_t_id][tmp_id] = {'gene':line.strip(), 't_start':tmp_t_start, 't_end':tmp_t_end, 't_range': tmp_t_end-tmp_t_start, 'mRNA':[], 'exon':[], 'CDS':[], 'coverage':0.0, 'identity':0.0, 'strand':tmp_strand}
        else:
            tmp_parent_id = 'NA'
            for tmp in tmp_desc_tokens:
                if( tmp.startswith('Parent') ):
                    tmp_parent_id = re.sub(r'^Parent=','',tmp).replace('.mrna','.path')
            
            if( tmp_parent_id == 'NA' ):
                continue
            if( not rv[tmp_t_id].has_key(tmp_parent_id) ):
                sys.stderr.write('Parent ID is not available:%s\n'%tmp_parent_id)
                continue
            if( tmp_type == 'mRNA' ):
                for tmp in tmp_desc_tokens:
                    if( tmp.startswith('coverage=') ):
                        rv[tmp_t_id][tmp_parent_id]['coverage'] = float(re.sub(r'^coverage=','',tmp))
                    if( tmp.startswith('identity=') ):
                        rv[tmp_t_id][tmp_parent_id]['identity'] = float(re.sub(r'^identity=','',tmp))
            rv[tmp_t_id][tmp_parent_id][tmp_type].append( line.strip() )
    f_gff.close()
    return rv

def filter_best_cov(tmp_gff):
    rv = dict()
    gid2tid = dict()
    best_cov_genes = dict()
    for tmp_tid in tmp_gff.keys():
        rv[ tmp_tid ] = dict()
        for tmp_gid in tmp_gff[tmp_tid].keys():
            tmp_gene_id = re.sub(r'.path[0-9]+$','',tmp_gid)
            gid2tid[tmp_gid] = tmp_tid
            if( not best_cov_genes.has_key(tmp_gene_id) ):
                best_cov_genes[tmp_gene_id] = {'gid':tmp_gid, 'tid':tmp_tid}
            else:
                prev_gid = best_cov_genes[tmp_gene_id]['gid']
                prev_tid = best_cov_genes[tmp_gene_id]['tid']
                if( tmp_gff[prev_tid][prev_gid]['coverage'] < tmp_gff[tmp_tid][tmp_gid]['coverage'] ):
                    best_cov_genes[tmp_gene_id]['gid'] = tmp_gid
                    best_cov_genes[tmp_gene_id]['tid'] = tmp_tid
                elif( tmp_gff[prev_tid][prev_gid]['coverage'] == tmp_gff[tmp_tid][tmp_gid]['coverage'] ):
                    if( tmp_gff[prev_tid][prev_gid]['identity'] < tmp_gff[tmp_tid][tmp_gid]['identity'] ):
                        best_cov_genes[tmp_gene_id]['gid'] = tmp_gid
                        best_cov_genes[tmp_gene_id]['tid'] = tmp_tid

    for tmp_gene_id in best_cov_genes.keys():
        tmp_gid = best_cov_genes[tmp_gene_id]['gid']
        tmp_tid = best_cov_genes[tmp_gene_id]['tid']
        rv[tmp_tid][tmp_gid] = tmp_gff[tmp_tid][tmp_gid]

    return rv

def filter_top2(tmp_gff,filename_top2):
    rv = dict()
    q2t = dict()
    f_top2 = open(filename_top2,'r')
    for line in f_top2:
        tokens = line.strip().split("\t")
        q2t[tokens[0]] = tokens[2]
    f_top2.close()

    for tmp_tid in tmp_gff.keys():
        for tmp_gid in tmp_gff[tmp_tid].keys():
            tmp_gene_id = re.sub(r'.path[0-9]+$','',tmp_gid)
            if( q2t.has_key(tmp_gene_id) and q2t[tmp_gene_id] == tmp_tid ):
                if( not rv.has_key(tmp_tid) ):
                    rv[tmp_tid] = dict()
                rv[tmp_tid][tmp_gid] = tmp_gff[tmp_tid][tmp_gid]
    return rv

def count_genes(tmp_gff):
    gene_list = []
    for tmp_tid in tmp_gff.keys():
        for tmp_gid in tmp_gff[tmp_tid].keys():
            gene_list.append( re.sub(r'.path[0-9]+$','',tmp_gid) )
    return len(set(gene_list))
