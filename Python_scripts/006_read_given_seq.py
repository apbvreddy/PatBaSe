import sys
from numpy import loadtxt
def split(seq):
        return list(seq)
ref_seq = sys.argv[1]
#cdcbaAAAaaaaaCDCCBAAAAAAAAbabbccbcccdcddddeede,f00211_E1_FluAB_FAM
ref_id = sys.argv[2]
file = open("wm2.csv")
numpy_array = loadtxt(file, delimiter=",",dtype=str)
print(len(numpy_array))
#print(numpy_array)
print(numpy_array[20,20])
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


file2 = open(sys.argv[3])
numpy_seq = loadtxt(file2, delimiter=",",dtype=str)
print(len(numpy_seq))
#print(numpy_seq)
#print(numpy_seq[5735,0])
print(ref_seq,ref_id,"----------------Refseq")
seq1=split(ref_seq)
for j in range(271):
    score=0
    #print(numpy_seq[j,0],j)
    seq2=split(numpy_seq[j,0])
    for k in range(46):
        #print(seq1[k],seq2[k])
        key=seq1[k]+seq2[k]
        score += int(wtmx[key])
    print(numpy_seq[j,0],j,score,numpy_seq[j,1])
