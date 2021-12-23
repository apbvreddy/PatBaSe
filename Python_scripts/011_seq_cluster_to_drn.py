import sys
import os
from numpy import loadtxt
def split(seq):
        return list(seq)
file = open("wm2.csv")
numpy_array = loadtxt(file, delimiter=",",dtype=str)
print(len(numpy_array))
#print(numpy_array)
#print(numpy_array[20,20])
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
#print(numpy_pwf[2,46])
#exit()

file2 = open(sys.argv[1])
SNO=sys.argv[2]
numpy_seq = loadtxt(file2, delimiter=",",dtype=str)
NoSeq=len(numpy_seq)
print(NoSeq)
PScut=float(sys.argv[3])
print(PScut)

for i in range(NoSeq):
    print(numpy_seq[i,1],numpy_seq[i,0],"------------",i)
    ocf=open(numpy_seq[i,1]+".txt",'w')
    seq1=split(numpy_seq[i,0])
    sseq=numpy_seq[i,0]
    sseq0=numpy_seq[i,1]
    for j in range(NoSeq):
        seq2=split(numpy_seq[j,0])
        if (j==0):
            seq2=seq1
            numpy_seq[i,0]=numpy_seq[0,0]
            numpy_seq[i,1]=numpy_seq[0,1]
            numpy_seq[0,0]=sseq
            numpy_seq[0,1]=sseq0
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
            if j==0:
                Score=score
            pscore=round(score/Score*100,2)
        if pscore < PScut:
                continue
        #print(numpy_seq[j,0],round(score,2),pscore,numpy_seq[j,1])
        print(numpy_seq[j,0],round(score,2),pscore,numpy_seq[j,1],file = ocf)
    ocf.close()

    I=str(i)
    cmd = "sort -n -r -t' ' -k2 "+numpy_seq[i,1]+".txt > "+numpy_seq[i,1]+"_cluster_"+SNO+".txt"
    print(cmd)
    os.system(cmd)
    
    cmd = "rm "+numpy_seq[i,1]+".txt"
    print(cmd)
    os.system(cmd)

    cmd = "cut -d' ' -f2,4 "+numpy_seq[i,1]+"_cluster_"+SNO+".txt | sort -n -r -t' ' -k 1| cut -d' ' -f2 > zzz.del" 
    print(cmd)
    os.system(cmd)
    
    cmd ="dos2unix zzz.del"
    print(cmd)
    os.system(cmd)

    cmd = "grep -v -f zzz.del  "+sys.argv[1]+" > "+I+"_"+sys.argv[1]
    print(cmd)
    os.system(cmd)
    
    '''
    cmd = "sed 's/^/grep /' t1.del | sed 's/$/ "+sys.argv[2]+" >> "+numpy_seq[i,1]+"cID_.csv/' > t"+I+".sh"
    print(cmd)
    os.system(cmd)
    
    cmd ="dos2unix t"+I+".del"
    print(cmd)
    os.system(cmd)    
    #cmd = "grep -f auto_"+I+"_compare.txt cIDg01to73_ampdRn_seq2.csv > autoplot_"+I+"_compare.csv"
    cmd="grep -f t"+I+".del "+sys.argv[2]+" > autoplot_"+I+"_compare.csv"
    print(cmd)
    os.system(cmd)

    cmd="grep -f t"+I+".del "+numpy_seq[i,1]+".txt | sort -n -r -t' ' -k3 > scoring_"+I+"_compare.csv"
    print(cmd)
    os.system(cmd)
      
    cmd1 = "rm "+numpy_seq[i,1]+".txt t"+I+".del"
    print(cmd1)
    os.system(cmd1)
    '''
    
    if i == 0:
        exit()

