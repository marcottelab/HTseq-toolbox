#!/bin/bash

#SBATCH -o bw2.o%j
#SBATCH -J "bw2.foo"

#$ -N bw2.foo

BOWTIE2="$HOME/src.HTseq/bowtie/2.0.6/bowtie2"
SAM2HIT="$HOME/git/HTseq-toolbox/sam/sam-to-sam_hit.py"
SAM2FREQ="$HOME/git/HTseq-toolbox/sam/sam_hit-to-t_freq.py"

## Thread: lonestar=12, stampede=16
NUM_THREADS=12

export BOWTIE2_INDEXES="$WORK/ens/bw2"
#export BOWTIE_2INDEXES="$WORK/ens/bw1/"
#DB="XENLA_2013may_longest_cdna_annot"
#DB="XENLA_JGIv7b"
DB="MOUSE_ens72_cdna_annot_longest"

#FQ="../fastq/OMRF20110730_XENLA_EGG1.paired.fastq"
for FQ in $(ls ../fastq/*.fastq)
do
  BASENAME=$(basename $FQ)
  BASENAME=${BASENAME/.fastq/}".$DB.bw2L_k10N0"
  SAM=$BASENAME".sam"
  $BOWTIE2 -q --local -k 10 -N 0 --threads $NUM_THREADS --reorder -x $DB -U $FQ -S $SAM
  $SAM2HIT $SAM
  $SAM2FREQ $SAM"_hit"
done

SAM2HIT="$HOME/git/HTseq-toolbox/tnseq/tnseq_sam-to-tnHit+gHit.py"
HIT2PAIR="$HOME/git/HTseq-toolbox/tnseq/tnHit+gHit-to-tnPair.py"

for SAM in $(ls *sam_hit)
do
  $SAM2HIT $SAM
  TN_HIT=$SAM"_tnHit"
  $HIT2PAIR $TN_HIT
done
#!/bin/bash
#$ -V
#$ -cwd
#$ -j y
#$ -o $JOB_NAME.o$JOB_ID
#$ -pe 1way 8
#$ -q long
#$ -l h_rt=24:00:00
#$ -M $EMAIL
#$ -m be
#$ -P hpc
set -x
#$ -N pair.L24

#SAM="Stacy201305_AGGACtn_Aerobic1.paired.AGGAC_ANH9381.bw_k10N0.sam_hit.gz"
#SAM="Stacy201305_AGGACtn_Aerobic2.paired.AGGAC_ANH9381.bw_k10N0.sam_hit.gz"
#SAM="Stacy201305_AGGACtn_Anaerobic1.paired.AGGAC_ANH9381.bw_k10N0.sam_hit.gz"
#SAM="Stacy201305_AGGACtn_Anaerobic2.paired.AGGAC_ANH9381.bw_k10N0.sam_hit.gz"
#SAM="Stacy201305_AGGACtn_LibBC21.paired.AGGAC_ANH9381.bw_k10N0.sam_hit.gz"
SAM="Stacy201305_AGGACtn_LibBC24.paired.AGGAC_ANH9381.bw_k10N0.sam_hit.gz"

./tnseq_sam-to-pair_dist.py $SAM
