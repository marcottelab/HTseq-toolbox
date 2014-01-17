#!/bin/bash
GFF=$1
TOP2=${GFF/_gff/_top2}
$HOME/git/HTseq-toolbox/gff/gff+top2-to-rep_gff-single.py $GFF $TOP2
