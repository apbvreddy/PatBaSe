
com='{printf "%s%s", $0, NR%2?",":ORS}'
#awk '{printf "%s%s", $0, NR%2?",":ORS}' $1
awk $com $1
