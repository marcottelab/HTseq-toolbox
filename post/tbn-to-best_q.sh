#!/bin/bash
for TBL in $(ls *Vee*tbn+_tbl)
do
  OUT=${TBL/tbn+_tbl/best_q}
  echo $OUT
  ./tbn-to-best_q.py $TBL > $OUT
done

#-rw-r--r-- 1 linusben G-25507 410M May  5 18:33 XENTR_ens66_pep.Amin201106_XENLA_nrC.tbn+_tbl
#-rw-r--r-- 1 linusben G-25507 300M May  5 20:44 XENTR_ens66_pep.Chung201110_XENLA_nrC.tbn+_tbl
#-rw-r--r-- 1 linusben G-25507 514M May  6 03:06 XENTR_ens66_pep.Park201106_XENLA_nrC.tbn+_tbl
#-rw-r--r-- 1 linusben G-25507 442M May  6 07:43 XENTR_ens66_pep.Quigley201112_XENLA_nrC.tbn+_tbl
#-rw-r--r-- 1 linusben G-25507 570M May 17 07:11 XENTR_ens66_pep.TXGP201107_XENLA_EGG_nrC.tbn+_tbl
