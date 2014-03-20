#!/bin/bash
for BASE_LOG in $(ls *base_log)
do
  echo $BASE_LOG
  $HOME/git/HTseq-toolbox/align/base_log-to-holes.py $BASE_LOG
done
