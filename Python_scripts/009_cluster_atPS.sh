#!/bin/bash

#cp seq73g01to73_NoAmpdRn_cID.csv test.csv

SP=$1;LS=$2;LE=$3
echo "Clustering at $SP percent similarity"

for (( n=$LS; n<=$LE; n++ ))
    do
    echo "ClusteringRound $n"
    echo "py /d/PatBSe_Project/Python_scripts/005_read_wtmx_seq_shield.py test.csv 00$n $SP"
    py /d/PatBSe_Project/Python_scripts/005_read_wtmx_seq_shield.py test.csv 00$n $SP
    echo "mv 0_test.csv test.csv"
    mv 0_test.csv test.csv
done
