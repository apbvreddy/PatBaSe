import pandas as pd
import openpyxl
import sys
import os

filename = sys.argv[1]
fi=open(filename,"r")
abcd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
      'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
c,r = 46,2
mxipfv=[[0 for x in range (c)] for y in range (r)]
ix=[0 for x in range(c)]
r1=fi.readline()
pf=r1.strip()
pfa=pf.split(",")
ns=pfa.pop(0)
#print(pfa)
mxipfv[0]=[int(i) for i in pfa]

r2=fi.readline()
pf=r2.strip()
pfa=pf.split(",")
ps=pfa.pop(0)
#print(pfa)
mxipfv[1]=[int(i) for i in pfa]

#print(ns,mxipfv[0])
#print(ps,mxipfv[1])
fi.readline()   #To skip the column lables
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
