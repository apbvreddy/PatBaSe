import pandas as pd
import openpyxl

### Read Amplification Data ######
df= pd.read_excel('excel_sheets.xlsx', sheet_name='Amplification Data',
    header=23,usecols = "B,C,D,F,G")
df.to_csv('AmplificationData.csv')

df= pd.read_excel('excel_sheets.xlsx', sheet_name='Results',
    header=23,usecols = "B,D,E, F,G,I,J,N,O,S,U,V")
df.to_csv('Results.csv')

f = open('AmplificationData.csv', "r")
f.readline()
i = int()
j = int()
tit = [range(46)]
fo = open("amp_data.csv", "a")
tit[0]='Well'
tit.append('Target')
for i in range(46):
    j=i+1
    tit.append('Round_'+str(i))
    if (j==46):
        stit=str(tit)
        ftit=stit.replace("[","")
        stit=ftit.replace("]","")
        #print(stit)
        fo.write(stit+"\n")
i=0
drn=[10.10,20.10]
for x in f:
    y=x.split(",")
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
        sdrn=str(drn)
        fdrn=sdrn.replace("[","")
        sdrn=fdrn.replace("]","")
        #print(sdrn)
        fo.write(sdrn+"\n")
        i=0
        #break

f.close()
fo.close()

f1 = open("Results.csv", "r")
f2 = open("amp_data.csv","r")
fo = open("amp_results.csv","w")
for x in f1:
    pf=x.strip()
    sf=f2.readline()
    ps=pf+","+sf
    print(ps)
    fo.write(ps)
f1.close()
f2.close()
fo.close()

