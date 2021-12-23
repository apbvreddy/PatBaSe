import pandas as pd
#import openpyxl
import sys
import os

filename = sys.argv[1]
skipR=int(sys.argv[2])

### Read Amplification Data ######
df=pd.read_excel(filename, sheet_name='Amplification Data',
    header=skipR,usecols = "A,B,D,F,G")
#Well	WellPosition	CycleNumber	Target	Rn	        dRn	        Sample	Omit
#1	A1	        1	        RSV	1187437.875	-16535.62274	S395_RP1	FALSE
df.to_csv('AmplificationData.csv')

df=pd.read_excel(filename, sheet_name='Results',
    header=skipR,usecols = "A,B,D,E,F,G,I,J,N,O,S")
#Well	Well Position	Omit	Sample	Target	Task	Reporter	Quencher	Amp Status	Amp Score	Curve Quality	Result Quality Issues		Cq	Cq Confidence	Cq Mean	Cq SD	Auto Threshold	Threshold	Auto Baseline	Baseline Start	Baseline End
#1	A1	FALSE	S395_RP1	RSV	UNKNOWN	ABY	None	No Amp	1.838318231	-103770	55612	159383	Undetermined	0			FALSE	75000	TRUE	5	45

df.to_csv('Results.csv')

fname,sfix=filename.split(".")

#Read AmplificationData.csv and write 46 recards to one recard
f = open('AmplificationData.csv', "r")
f.readline()
i = int()
j = int()
tit = []
fo = open("amp_data.csv", "w")
tit.append('Well')
tit.append('WellPos')
tit.append('Target')
tit.append('LoD')
#print(str(tit))
for i in range(46):
    #print(str(tit))
    j=i+3
    tit.append('Cycle_'+str(i))
    #print(j)
stit=str(tit)
ftit=stit.replace("[", "")
stit=ftit.replace("]", "")
fo.write(stit+"\n")
drn=[]
i=0
for x in f:
    y=x.split(",")
    if i==0:
        #print(x)
        #print(y)
        #print(y[1],y[2],y[3],y[5])
        drn=[]
        drn.append(y[1])
        drn.append(y[2])
        drn.append(y[3])
        drn.append(y[5])
        #print(drn)
    drn.append(round(float(y[4]),))
    i+=1
    if i==46:
        sdrn=str(drn)
        fdrn=sdrn.replace("[","")
        mdrn=fdrn.replace("\\n","")
        sdrn=mdrn.replace("]","")
        i=0
        #print(sdrn)
        fo.write(sdrn+"\n")
        
f.close()
fo.close()

f1 = open("Results.csv", "r")
f2 = open("amp_data.csv","r")
fo = open(fname+"_ampdRn_results.csv","w")
for x in f1:
    pf=x.strip()
    pfa=pf.split(",")
    #print(pfa[6])
    sf=f2.readline()
    ps1=fname+","+pf+","+sf
    ps=ps1.replace(" A/B","AB")
    fo.write(ps)
f1.close()
f2.close()
# Delete intermediate files
os.remove("Results.csv")
os.remove("amp_data.csv")
os.remove("AmplificationData.csv")
fo.close()

