import pandas as pd
import openpyxl
import sys
import os

filename = sys.argv[1]
target = sys.argv[2]
opfile = target+filename

fi = open(filename,"r")
tit=fi.readline()
tit1=tit.split(",")
tit=tit1[16:63]
tit[0]="CurveID"
#print(','.join(tit))

r,c = 2,46
mxipfv = [[0 for x in range(c)] for y in range(r)]

'''
for r in mxipfv:
        print(r)
'''

fo = open(opfile,"w")
fo.write(",".join(tit))
sys.stdout = fo

for x in fi:
    pf=x.strip()
    #print(pf)
    pfa=pf.split(",")
    pfs=pfa[0]+"_"+pfa[5]+"_"+pfa[7]+"_"+pfa[2]+"_"+pfa[3]+","
    pfv=pfa[17:63]
    ipfv=[int(i) for i in pfv]
    j=0
    for r in ipfv:
        #print(j)
        if r < 0:
            if mxipfv[0][j] > r:
                mxipfv[0][j]=r
        elif r > 0:
            if mxipfv[1][j] <= r:
                mxipfv[1][j]=r
        j=j+1
    print(pfs,ipfv)
    #print(pfs,mxipfv[0])
    #print(pfs,mxipfv[1])
fi.close()

print("LowestValue,",mxipfv[0])
print("HighestValue,",mxipfv[1])
fo.close()

