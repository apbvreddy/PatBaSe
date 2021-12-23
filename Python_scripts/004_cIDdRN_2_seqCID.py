import pandas as pd
import openpyxl
import sys
import os


abcd=['a','b','c','d','e','f','g','h','i','j']
ABCD=['A','B','C','D','E','F','G','H','I','J']
c,r = 46,4
mxipfv=[[0 for x in range (c)] for y in range (r)]
ix=[0 for x in range(c)]

# Read extreme dRn values and weight factor values 4rows

filename = sys.argv[1]
fi=open(filename,"r")
nps=[]
for k in range(r):
    r1=fi.readline()
    pf=r1.strip()
    pfa=pf.split(",")
    nps.append(pfa.pop(0))
    #print(pfa)
    mxipfv[k]=[float(i) for i in pfa]
    #print(nps[k],mxipfv[k])
 
# Read Title line, curveID and dRn value recards 20823
fi.readline()   #To skip the column lables

# Convert dRn Values to sequence pattern and write into file
wf = open("seq"+filename,"w")
for x in fi:
    pf=x.strip()
    #print(pf)
    pfa=pf.split(",")
    curveID=pfa.pop(0)
    #print(curveID,pfa[0])
    ax=""
    for j in range(c):
        if int(pfa[j]) < 0 :
            #print(pfa[j],mxipfv[0][j])
            ix[j]=int(float(pfa[j])/float(mxipfv[0][j]))
            if ix[j] >= 10:
                ix[j] = 9
            #print(abcd[ix[j]],f"{ix[j]:.0f}")
            ax+=abcd[ix[j]]
        elif int(pfa[j]) >= 0 :
            #print(pfa[j],mxipfv[1][j])
            ix[j]=int(float(pfa[j])/float(mxipfv[1][j]))
            if ix[j] >= 10:
                ix[j] = 9
            #print(ABCD[ix[j]],f"{ix[j]:.0f}")
            ax+=ABCD[ix[j]]

    #print(ix)
    print(ax+","+curveID)
    wf.write(ax+","+curveID+"\n")
fi.close()
wf.close()
