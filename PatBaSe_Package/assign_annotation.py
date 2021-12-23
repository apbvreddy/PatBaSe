import pandas as pd
import openpyxl
import sys
import os

from numpy import loadtxt

#Read consicutive recards and extract cIDs,Stat
def assign_annotation(queryf,refannf):
    
    ip1=open(queryf,"r")
    numpy_seq = loadtxt(ip1, delimiter=" ",dtype=str)
    #print(numpy_seq)
    NoSeq=len(numpy_seq)
    print(NoSeq)
    ns=int(NoSeq)/2
    for i in range(ns):
        
        r1=ip1.readline()
        r2=ip2.readline()

        pf2=r1.strip()
        pf2=r2.strip()
    
        pfa1=pf.split(" ")
        pfa2=pf.split(" ")
        
        print(r1,r2)

queryf="test000013_yesRelatedReference.csv"
refannf="../patebase_internaldata/80p_rep_cID_annotations.csv"
def assign_annotation(queryf,refannf):
    '''
        
    ip2=open(refannf,"r")
    
    for k in ip2:
        r3=ip2.readline()
        pf=r3.strip()
        pfa=pf.split(",")
        nps.append(pfa.pop(0))
        #print(pfa)
        mxipfv[k]=[float(i) for i in pfa]
        #
        print(nps[k],mxipfv[k])
    fi.close()
    ''' 
