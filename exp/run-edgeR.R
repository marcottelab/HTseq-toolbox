args <- commandArgs(trailingOnly = TRUE)

filename_in <- args[1]
sample1 <- args[2]
sample2 <- args[3]
min_cpm1 <- args[4]

filename_base <- sub('.edgeR_in','',filename_in)
filename_cpm <- sub('.edgeR_in','.edgeR_cpm',filename_in)

library(edgeR)

x <- read.delim(filename_in,row.names='ID',header=T)
groups <- gsub('_0[1234]$','',colnames(x))
keep <- rowSums(cpm(x)>1) >= min_cpm1
x <- x[keep,]

y <- DGEList(counts=x,group=groups)
y <- calcNormFactors(y)
y <- estimateCommonDisp(y)
y <- estimateTagwiseDisp(y)

write.table(cpm(x), file=filename_cpm, row.names=TRUE, col.names=TRUE, sep='\t')

write.table(topTags(exactTest(y,pair=c(sample2,sample1)),n=Inf), paste(filename_base,paste(sample1,sample2,sep='-'),'edgeR_out',sep='.'),sep='\t')
