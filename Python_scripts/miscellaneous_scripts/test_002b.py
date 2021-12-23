import openpyxl
import sys

filename = sys.argv[-1]
f1 = open(filename, "r")
st=[range(14,19)]
md=[range(19,44)]
ed=[range(44,60)]
sts=float()
for x in f1:
    ral=f1.readline()
    print(ral)
    arl=ral.split(",")
    for i in range(len(st)):
        sts += float(arl(st[i]))
        print(arl[14:19])
        print(sts)
        
f1.close()

