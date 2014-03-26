#!/usr/bin/Rscript

args <- commandArgs(trailingOnly = TRUE)

filename_tbl <- args[1]

dataset_name <- sub('.rpkm.txt','_rpkm',filename_tbl)

exp_table <- read.table(file=filename_tbl,header=T,row.names='ID',stringsAsFactors=FALSE,sep="\t")

tmp_cor <- dist( 1 - cor(as.matrix(exp_table),method='spearman') )
tmp_clust <- hclust( tmp_cor, method="average")
png(filename=paste(dataset_name,".SpR_clust.color.png",sep=''),
        width=1024,height=640);
plot(tmp_clust, main=paste(dataset_name,":hclust_SpR_average",sep=''))
dev.off();

tmp_cor <- dist( t(as.matrix(exp_table)), method='euclidean' )
tmp_clust <- hclust( tmp_cor, method="average")
png(filename=paste(dataset_name,".dist_clust.color.png",sep=''),
        width=1024,height=640);
plot(tmp_clust, main=paste(dataset_name,":hclust_dist_average",sep=''))
dev.off();

png(filename=paste(dataset_name,".boxplot.png",sep=''),
        width=1024,height=640);
boxplot(as.matrix(exp_table), outline=FALSE, notch=TRUE, las=2, main=dataset_name)
dev.off();
