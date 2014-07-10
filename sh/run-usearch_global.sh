#!/bin/bash
USEARCH="$HOME/src/usearch/usearch7.0.1090_i86linux32"
USER_FIELDS='query+target+id+alnlen+mism+gaps+ql+qlo+qhi+tl+tlo+thi+evalue+bits+qstrand+tstrand'

QUERY_FA='eggnogv4_NOG_rep.fa'
DB_FA=$QUERY_FA

OUT=$(basename $QUERY_FA)"."$(basename $DB_FA)".usearch_tbl"
if [ $QUERY_FA == $DB_FA ]; then
  OUT=$(basename $QUERY_FA)".self.usearch_tbl"
fi

OUT=$(echo $OUT | sed -e 's/.fa[sta]*././g')

$USEARCH -usearch_global $QUERY_FA -db $DB_FA -id 0.4 -maxaccepts 16 -maxrejects 32 -userout $OUT -userfields $USER_FIELDS
