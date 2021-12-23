import sys
from numpy import loadtxt
def split(seq):
    return list(seq)
ref_seq = sys.argv[2]
#cdcbaAAAaaaaaCDCCBAAAAAAAAbabbccbcccdcddddeede

ref_id = sys.argv[3]
#f00211_E1_FluAB_FAM
file = open("wm2.csv","r")
numpy_array = loadtxt(file, delimiter=",",dtype=str)
print("length_numpy_array = ",len(numpy_array))
#print(numpy_array)
print("numpy_array = ",numpy_array[20,20])
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

#file2 = open("seqALLf00201_30_curveID_dRn.csv")
file2 = open(sys.argv[1])
#seqcIDg01to73_ampdRn02_bubble.csv

numpy_seq = loadtxt(file2, delimiter=",",dtype=str)
print("length_numpy_seq = ",len(numpy_seq))
#print(numpy_seq)
#print(numpy_seq[5735,0])
print(ref_seq,ref_id,"----------------QuerySeq")
seq1=split(ref_seq)
ll=len(seq1)
#Max score calculations
scoreMax=0
for i in range(ll):
    key=seq1[i]+seq1[i]
    scoreMax +=int(wtmx[key])

ll1=46-ll+1

for j in range(267):
    #print(numpy_seq[j,0],j,"----------------SubjectSeq")
    seq2=split(numpy_seq[j,0])
    Score=0
    sequence2=""
    for k in range(ll1):
        score=0
        if k>0:
            sequence2=sequence2+" "
            #print(sequence2+"end")
        for i in range(ll):
            k2=k+i
            #print(seq1[i],seq2[k2])
            key=seq1[i]+seq2[k2]
            pos=str(i)+" "+str(k2)
            #print(key,pos)
            score += int(wtmx[key])
        if score > Score:
            Score=score
            pScore=float(Score/scoreMax)*100
            fps="{:.2f}".format(pScore)
            K=str(k)
            K2=str(k2)
            #print(str(Score))
            ali_seq2=sequence2+ref_seq+" "+ref_id+" <----------------QuerySeq"
    print(numpy_seq[j,0],j,Score,fps,K,K2,numpy_seq[j,1],"-----SubjectSequence")
    print(ali_seq2)
