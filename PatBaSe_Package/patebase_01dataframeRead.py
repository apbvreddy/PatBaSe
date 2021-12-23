import pandas as pd
import openpyxl
import sys
import os

filename=sys.argv[1]
fname,sfix=filename.split(".")

def read_excelSheet(sheetName="Amplification Data",columns="A,B,D,F,G",sheetFName="AmplificationData"):
    ddf=pd.read_excel(filename,sheetName,header=20)
    skipR=0
    for index, row in ddf.iterrows():
        print(row[0])
        if row[0] == "Well":
            skipR = index+21
            break                
    print(skipR)
    df=pd.read_excel(filename, sheet_name=sheetName,
        header=skipR,usecols = columns)
    df.to_csv(sheetFName+'.csv')

def creat_ampDataF(ADF,PADF):
#Read AmplificationData.csv and write 46 recards to one recard
    f = open(ADF,"r")
    f.readline()
    #i = int()
    #j = int()
    tit = []
    fo = open(PADF, "w")
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

def create_AmpdRn_results(RES,AmpdRn,COMB):
    f1 = open(RES,"r")
    f1tit=f1.readline()
    f1s=f1tit.strip()
    f2 = open(AmpdRn,"r")
    f2tit=f2.readline()
    fo = open(COMB,"w")
    fo.write("FileID,"+f1s+","+f2tit)
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
    fo.close()

def compareTargetCallAmpRes(COMB,TCall,COMBC):
    f1=open(TCall,'r')
    f1.readline()
    f2=open(COMB,'r')
    f2tit=f2.readline()
    fop=open(COMBC,'w')
    fop.write(f2tit)
    for x1 in f1:
        x=x1.replace(" A/B","AB")
        y=x.split(",")
        x2=f2.readline()
        z=x2.split(",")
        #print(x,x2)
        #print(y[1],y[4],z[3],z[5])
        y14=y[1]+"_"+y[4]
        z35=z[3]+"_"+z[5]
        while y14 != z35:
            x2=f2.readline()
            z=x2.split(",")
            z35=z[3]+"_"+z[5]
        #print(y14,z35)
        #print(z[8])
        if z[8] == "Amp":
            continue
        #print(x2)
        fop.write(x2)

    f1.close()
    f2.close()
    fop.close()
    '''
    cmd="sed \"s/'//g\" t"+COMBC+" > "+COMBC
    print(cmd)
    os.system(cmd)
    '''

def create_cIDdRn(infile,outfile):
    fi = open(infile,"r")
    tit=fi.readline()
    tit1=tit.split(",")
    tit=tit1[16:63]
    tit[0]="CurveID"
    #print(','.join(tit))

    r,c = 2,46
    mxipfv = [[0 for x in range(c)] for y in range(r)]

    fo = open(outfile,"w")
    fo.write(",".join(tit))
    sys.stdout = fo
    for x in fi:
        pf=x.strip()
        #print(pf)
        pfa=pf.split(",")
        pfa2=str(round(float(pfa[2])))
        pfs=pfa[0]+"_"+pfa[5]+"_"+pfa[7]+"_"+pfa2+"_"+pfa[3]+","
        pfv=pfa[17:63]
        ipfv=[int(i) for i in pfv]
        j=0
        for r in ipfv:
            #print(j)
            if r < 0:
                if mxipfv[0][j] > r:
                    mxipfv[0][j]=r
            elif r > 0:
                if mxipfv[1][j] <= r:
                    mxipfv[1][j]=r
            j=j+1
        print(pfs,ipfv)
        #print(pfs,mxipfv[0])
        #print(pfs,mxipfv[1])
    print("LowestValue,",mxipfv[0])
    print("HighestValue,",mxipfv[1])
    fi.close()
    fo.close()

#CharecterPair Matrix
def dRn_to_LetterSeq(rws_pwm,cIDdRn,cIDseq):
    abcd=['a','b','c','d','e','f','g','h','i','j']
    ABCD=['A','B','C','D','E','F','G','H','I','J']
    c,r = 46,4
    mxipfv=[[0 for x in range (c)] for y in range (r)]
    ix=[0 for x in range(c)]
    # Read extreme dRn values and weight factor values 4rows
    fi=open(rws_pwm,"r")
    nps=[]
    r1=fi.readline()
    pf=r1.strip()
    pfa=pf.split(",")
    print(pfa)
    for k in range(r):
        r1=fi.readline()
        pf=r1.strip()
        pfa=pf.split(",")
        nps.append(pfa.pop(0))
        #print(pfa)
        mxipfv[k]=[float(i) for i in pfa]
        print(nps[k],mxipfv[k])
    fi.close()
    fi=open(cIDdRn,"r")
    #   Read Title line, curveID and dRn value recards
    rt=fi.readline()
    #   Convert dRn Values to sequence pattern and write into file
    wf = open(cIDseq,"w")
    for x in fi:
        pf=x.strip()
        pf1=pf.replace("[", "")
        pf=pf1.replace("]", "")
        #print(pf)
        pfa=pf.split(",")
        curveID=pfa.pop(0)
        if curveID=="LowestValue":
            continue
        if curveID=="HighestValue":
            continue
        #print(curveID,pfa[0])
        ax=""
        for j in range(c):
            if int(pfa[j]) < 0 :
                #print(pfa[j],mxipfv[0][j])
                ix[j]=int(float(pfa[j])/float(mxipfv[0][j]))
                if ix[j] >= 10:
                    ix[j] = 9
                #print(abcd[ix[j]],f"{ix[j]:.0f}")
                ax+=abcd[ix[j]]
            elif int(pfa[j]) >= 0 :
                #print(pfa[j],mxipfv[1][j])
                ix[j]=int(float(pfa[j])/float(mxipfv[1][j]))
                if ix[j] >= 10:
                    ix[j] = 9
                #print(ABCD[ix[j]],f"{ix[j]:.0f}")
                ax+=ABCD[ix[j]]
        #print(ix)
        print(ax+","+curveID)
        wf.write(ax+","+curveID+"\n")
    fi.close()
    wf.close()

def main(fname):

    #pbid = "/d/PatBaSe_Project/PatBaSe_Package/patebase_internaldata"
    pbid = "patebase_internaldata"
#    '''
#Read Results Sheet
    sheetName = 'Results'
    columns = "A,B,D,E,F,G,I,J,N,O,S"
    sheetFName=fname+"_Results"
    print("----->Reading Excel Sheet "+sheetName)
    read_excelSheet(sheetName,columns,sheetFName)

#Read Target Call Sheet
    sheetName = 'Target Call'
    columns = "A,B,C,D,E,F,G,H"
    sheetFName=fname+"_TargetCall"
    print("----->Reading Excel Sheet "+sheetName)
    read_excelSheet(sheetName,columns,sheetFName)
    
#Read Amplification Data Sheet
    sheetName = 'Amplification Data'
    columns="A,B,D,F,G"
    sheetFName=fname+"_AmplificationData"
    print("----->Reading Excel Sheet "+sheetName)
    read_excelSheet(sheetName,columns,sheetFName)
   
#Reformat AmplificationData.csv
    ADF=fname+"_AmplificationData.csv"
    PADF=fname+'_amp_data.csv'
    print("----->Creating csv file "+PADF)
    creat_ampDataF(ADF,PADF)
    
#Combinf Results.csv & AmplificationData.csv    
    RES = fname+"_Results.csv"
    AmpdRn = fname+"_amp_data.csv"
    COMB = fname+"_ampdRn_results.csv"
    print("----->Creating "+fname+"_amp_data.csv")
    create_AmpdRn_results(RES,AmpdRn,COMB)
    
#Delete empty Sample Wells    
    COMB = fname+"_ampdRn_results.csv"
    TCall = fname+"_TargetCall.csv"
    COMBC = fname+"_tdwdRn.csv"
    print("----->Eliminating empty sample Wells")
    compareTargetCallAmpRes(COMB,TCall,COMBC)
    
#Convert to only curveID(cID) and curveData
    tdwdRn=fname+"_tdwdRn.csv"
    cIDdRn = fname+"_cIDdRn.csv"
    print("----->Creating cID and dRN value file")
    create_cIDdRn(tdwdRn,cIDdRn)
#    '''
   
#To read row_dev values and position weight matrix
    rws_pwm = pbid+"/positional_weight_factors.csv"
    #rws_pwm="../patebase_internaldata/positional_weight_factors.csv"
    cIDdRn=fname+"_cIDdRn.csv"
    cIDseq=fname+"_cIDseq.csv"
    print("----->generate_cIDseq file")
    dRn_to_LetterSeq(rws_pwm,cIDdRn,cIDseq)
    
# Delete intermediate files
    '''
    print ("----->Deleting intermediate data files")
    os.remove(fname+"_Results.csv")
    os.remove(fname+"_amp_data.csv")
    os.remove(fname+"_AmplificationData.csv")
    os.remove(fname+"_TargetCall.csv")
    os.remove(COMB)
    os.remove(tdwdRn)
    '''
#Execute main() function
if __name__ == '__main__':
    main(fname)
