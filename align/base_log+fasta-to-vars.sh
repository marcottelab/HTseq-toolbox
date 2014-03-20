#!/bin/bash
for BASE_LOG in $(ls *base_log)
do
  echo $BASE_LOG
  ./base_log+fasta-to-vars.py $BASE_LOG ../genome/168/BACSU_168.genome.fa 
done
