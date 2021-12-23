import sys
import os
from numpy import loadtxt
def split(seq):
    return list(seq)

f1 = open(sys.argv[1],"r")
# g000007_FluAB_FAM_20_B8_6_38_sub.txt

f2 = open(sys.argv[2],"r")
#cIDg01to73_ampdRn_bubble.csv
kvmx={}
for x in f2:
    #print (x)
    y=x.split(", ")
    kvmx[y[0]]=y[1:]
    print (kvmx[y[0]])
f2.close()

fo1=open(sys.argv[3],"w")
#output file
k=0
percentSim = float(sys.argv[4])
for x in f1:
    #print(x)
    y=x.split(" ")
    #print(y)
    seq1=y[0]
    st=int(y[4])
    en=int(y[5])+1
    pc=float(y[3])
    Y=y[6]+"_"+y[4]+"_"+y[5]
    if pc >percentSim :
        print(seq1[st:  en:],y[1],y[2],y[3],Y)
        L="Y+kvmx[y[6]][st:en]"
        fo1.write(L)
    elif exit():
        f1.close()
    #Y=y[6]+"_"+y[4]+"_"+y[5]
    
    #cmd="grep "+Y+" cIDg01to73_ampdRn_bubble.csv >> cIDg01to73_ampdRn_bubble_dRn.csv"
    #print(cmd)
    #os.system(cmd)
    k+=1
    if k==5:
        fo1.close()
        exit()
        
