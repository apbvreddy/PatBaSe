import sys
import os

filename = sys.argv[1]
fi=open(filename,"r")
for j in range(46):
        
    cut -d',' -f$1 test_ave_extreme_dRn.csv | sort -n -r > t$1.del
    awk -v var="Cycle" '$0~var{print NR}' t$1.del >> ttt$1.del


fi.close()
wf.close()
