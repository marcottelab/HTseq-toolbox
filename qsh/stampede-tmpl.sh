#!/bin/bash
#SBATCH -n 16
#SBATCH -t 24:00:00
#SBATCH --mail-user=$EMAIL
# #SBATCH --mail-type=ALL

# #SBATCH -p normal
# #SBATCH -o foo.o%j
# #SBATCH -J "foo.bar"

set -x

# put your script below.
./run.sh
