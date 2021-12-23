import pandas as pd
import openpyxl

df= pd.read_excel('excel_sheets.xlsx', sheet_name='Amplification Data',
    header=23,usecols = "B,C,D,F,G")

df.to_csv('bvb2.csv')

f = open("bvb2.csv", "r")
f.readline()
i = int()
j = int()
tit = [range(46)]
tit[0]='Well'
tit.append('Target')
for i in range(46):
    j=i+1
    tit.append('Round_'+str(i))
    if (j==46):
        print(tit) 
i=0
drn=[10.10,20.10]
for x in f:
    #x.rstrip("\n")
    #x.splitlines()
    y=x.split(",")
    #print(i,y[5])
    #print(len(drn))
    if i==0:
        drn[0]=y[1]
        drn[1]=y[3]
        j=2
    if j<len(drn):
        drn[j]=round(float(y[4]),)
    else:
        drn.append(round(float(y[4]),))
    i+=1
    j+=1
    if (i==46):
        print(drn)
        i=0
        #break

f.close()
