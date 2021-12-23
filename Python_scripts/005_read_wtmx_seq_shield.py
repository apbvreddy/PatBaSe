import sys
import os
from numpy import loadtxt
def split(seq):
        return list(seq)
file = open("wm2.csv")
numpy_array = loadtxt(file, delimiter=",",dtype=str)
print(len(numpy_array))
wtmx={}
for j in range(21):
    if j==0:
        continue
    for i in range(21):
        if i==0:
            continue
        #print(numpy_array[j,0],numpy_array[0,i])
        key=numpy_array[j,0]+numpy_array[0,i]
        wtmx[key]=numpy_array[j,i]
        #print(key,"=",wtmx[key])

pwf_file = open("positional_weight_factors.csv")
numpy_pwf = loadtxt(pwf_file, delimiter=",",dtype=str)
print(len(numpy_pwf))
#print(numpy_pwf)

file2 = open(sys.argv[1])
numpy_seq = loadtxt(file2, delimiter=",",dtype=str)
print(numpy_seq)

NoSeq=len(numpy_seq)
p1="Number of Sequences = "+str(NoSeq)
print(p1)

file3 = open(sys.argv[2])
numpy_seq0 = loadtxt(file3, delimiter=",",dtype=str)
NoSeq0=len(numpy_seq0)
p1="Number of Sequences = "+str(NoSeq0)
print(p1)

PScut=float(sys.argv[3])
print("Percent of Similarity = "+str(PScut))

for i in range(NoSeq):
    I=str(i+2849)
    print(I)
    print(numpy_seq[i,0]+numpy_seq[i,1]+I+"--------"+I)
    ocf=open(numpy_seq[i,1]+"_"+I+".txt","w")
    seq1=split(numpy_seq[i,0])
    seq2=split(numpy_seq[i,0])
    score=0
    for k in range(46):
        k1=k+1
        #print(seq1[k],ord(seq1[k]),seq2[k],ord(seq2[k]))
        # >64 & <75 = Capital  >96 & <107 = Small
        if ord(seq1[k]) < 75:
            mf=float(numpy_pwf[2,k1])
        elif ord(seq1[k]) > 96:
            mf=float(numpy_pwf[1,k1])
        #print(seq1[k],ord(seq1[k]),numpy_pwf[1,k1],seq2[k],ord(seq2[k]),numpy_pwf[2,k1],mf)
        key=seq1[k]+seq2[k]
        score += int(wtmx[key])*mf
    pscore=round(score/score*100,2)
    Score=score
    print(numpy_seq[i,0],round(score,2),pscore,numpy_seq[i,1],file = ocf)
    for j in range(NoSeq0):
        if numpy_seq[i,1] == numpy_seq0[j,1]:
            print(numpy_seq[i,1],numpy_seq0[j,1])
            continue
        seq2=split(numpy_seq0[j,0])
        score=0
        for k in range(46): 
            k1=k+1
            #print(seq1[k],ord(seq1[k]),seq2[k],ord(seq2[k]))
            # >64 & <75 = Capital  >96 & <107 = Small
            if ord(seq1[k]) < 75:
                mf=float(numpy_pwf[2,k1])
            elif ord(seq1[k]) > 96:
                mf=float(numpy_pwf[1,k1])
            #print(seq1[k],ord(seq1[k]),numpy_pwf[1,k1],seq2[k],ord(seq2[k]),numpy_pwf[2,k1],mf)
            key=seq1[k]+seq2[k]
            score += int(wtmx[key])*mf
            pscore=round(score/Score*100,2)
        if pscore < PScut:
                continue
        #print(numpy_seq0[j,0],round(score,2),pscore,numpy_seq[j,1])
        print(numpy_seq0[j,0],round(score,2),pscore,numpy_seq0[j,1],file = ocf)
    ocf.close()
