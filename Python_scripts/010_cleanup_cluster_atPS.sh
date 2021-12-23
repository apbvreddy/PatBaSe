#!/bin/bash

#Pi=$1
ls -alt | grep ' 79 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 80 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 81 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 82 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 83 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 84 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 85 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 86 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 87 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh
ls -alt | grep ' 88 ' | sed 's/\s */ /g' | cut -d' ' -f9- | sed 's/^/rm -rf /' >> t79_84.sh

./t79_84.sh
cut -d' ' -f3 t79_84.sh > $1p_unique_member_clusters.txt1
rm -rf t79_84.sh
sort -n -t'_' -k7 $1p_unique_member_clusters.txt1 >> $1p_unique_member_clusters.txt
wc $1p_unique_member_clusters.txt
wc *_cluster_00*.txt | sed 's/^ *//' | cut -d' ' -f1 | sort | uniq -c | sort -n | sed 's/^ *//' | sort -n -t' ' -k2
