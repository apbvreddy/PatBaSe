import pandas as pd
import openpyxl
import sys
import os
from numpy import loadtxt

filename=sys.argv[1]
fname,sfix=filename.split(".")

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
    #print(pfa)
    for k in range(r):
        r1=fi.readline()
        pf=r1.strip()
        pfa=pf.split(",")
        nps.append(pfa.pop(0))
        #print(pfa)
        mxipfv[k]=[float(i) for i in pfa]
        #
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
        #print(ax+","+curveID)
        wf.write(ax+","+curveID+"\n")
    fi.close()
    wf.close()
#-----------------------------------------------------------------------
    
def read_refcIDwm2(cIDseq,ref_seqcID,ref_cID,pwf,wm2,PScut):

#    import sys
#    import os

    def split(seq):
        return list(seq)
    file = open(wm2)
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
    pwf_file = open(pwf)
    numpy_pwf = loadtxt(pwf_file, delimiter=",",dtype=str)
    print(len(numpy_pwf))
    #print(numpy_pwf)

    file2 = open(cIDseq)    #Ref seq cID
    numpy_seq = loadtxt(file2, delimiter=",",dtype=str)
    #print(numpy_seq)
    NoSeq=len(numpy_seq)
    p1="Number of Sequence Pattern curces in new EDS file= "+str(NoSeq)
    print(p1)

    file3 = open(ref_seqcID)    #New file seq_cID
    numpy_seq0 = loadtxt(file3, delimiter=",",dtype=str)
    NoSeq0=len(numpy_seq0)
    p1="Number of Sequence Patterns curves in Reference Sequences = "+str(NoSeq0)
    print(p1)

    #PScut=80.0
    #PScut=70.0
    print("Percent of Similarity = "+str(PScut))

    nRR=fname+"_noRelatedReference.csv"
    if os.path.exists(nRR):
        os.remove(nRR)
    yRR=fname+"_yesRelatedReference.csv"
    if os.path.exists(yRR):
        os.remove(yRR)
    pRR=fname+"_pairRelatedReference.csv"
    if os.path.exists(pRR):
        os.remove(pRR)
      
    for i in range(NoSeq):
        I=str(i)
        #print(numpy_seq[i,0]+","+numpy_seq[i,1]+"--------"+I)
        newCfile = numpy_seq[i,1]+"_"+I+".txt"
        ocf=open(newCfile,"w")
        seq1=split(numpy_seq[i,0])
        seq2=split(numpy_seq[i,0])
        score=0
        for k in range(46):
            k1=k+1
            #print(seq1[k],ord(seq1[k]),seq2[k],ord(seq2[k]))
            # >64 & <75 = Capital  >96 & <107 = Small
            if ord(seq1[k]) < 75:
                mf=float(numpy_pwf[4,k1])
            elif ord(seq1[k]) > 96:
                mf=float(numpy_pwf[3,k1])
            #print(seq1[k],ord(seq1[k]),numpy_pwf[3,k1],seq2[k],ord(seq2[k]),numpy_pwf[4,k1],mf)
            key=seq1[k]+seq2[k]
            score += int(wtmx[key])*mf
        pscore=round(score/score*100,2)
        Score=score
        print(numpy_seq[i,0],round(score,2),pscore,numpy_seq[i,1],file = ocf)
        simc=0
        for j in range(NoSeq0):
            if numpy_seq[i,1] == numpy_seq0[j,1]:
                print(numpy_seq[i,1],numpy_seq0[j,1])
                continue
            seq2=split(numpy_seq0[j,0])
            score=0
            seg_score=[]
            for k in range(46): 
                k1=k+1
                #print(seq1[k],ord(seq1[k]),seq2[k],ord(seq2[k]))
                # >64 & <75 = Capital  >96 & <107 = Small
                if ord(seq1[k]) < 75:
                    mf=float(numpy_pwf[4,k1])
                elif ord(seq1[k]) > 96:
                    mf=float(numpy_pwf[3,k1])
                #print(seq1[k],ord(seq1[k]),numpy_pwf[3,k1],seq2[k],ord(seq2[k]),numpy_pwf[4,k1],mf)
                key=seq1[k]+seq2[k]
                score += int(wtmx[key])*mf
                pscore=round(score/Score*100,2)
            if pscore < PScut:
                continue
            #print(numpy_seq0[j,0],round(score,2),pscore,numpy_seq[j,1])
            print(numpy_seq0[j,0],round(score,2),pscore,numpy_seq0[j,1],file = ocf)
            simc += 1
        ocf.close()
        if simc==0:
            os.system("cat "+newCfile+" >> "+nRR)
            os.remove(newCfile)
        else:
            com_pRR = "sort -n -r -k2 "+newCfile+" | head -2 >> "+pRR
            os.system(com_pRR)
            com_yRR = "sed 's/ /,/g' "+pRR+" > "+yRR
            os.system(com_yRR)
            os.remove(newCfile)
#-----------------------------------------------------------------------

def assign_annotation(queryf,refannf,cIDdRnf,cIDdRnAnn):
    ip1=open(queryf,"r")
    numpy_seq = loadtxt(ip1,delimiter=",",dtype=str)
    NoSeq=len(numpy_seq)
    print(queryf,NoSeq)
    
    ip2=open(cIDdRnf,"r")
    numpy_dRn = loadtxt(ip2,delimiter=",",dtype=str)
    NoSeq2=len(numpy_dRn)
    print(cIDdRnf,NoSeq2)
    
    ip3=open(refannf,"r")
    numpy_ann = loadtxt(ip3,delimiter=",",dtype=str)
    NoSeq3=len(numpy_ann)
    print(refannf,NoSeq3)

    opf=open(cIDdRnAnn,"w")
    for i in range(int(NoSeq)):
        if i % 2==0:
            #print(numpy_seq[i][3],numpy_seq[i][0],numpy_seq[i+1][1],numpy_seq[i+1][2],numpy_seq[i+1][3])
            
#            '''
            for k in range(int(NoSeq3)):
                #print(numpy_dRn[k][0],numpy_seq[i+1][3])
                if numpy_seq[i+1][3] == numpy_ann[k][0]:
                    result=numpy_seq[i][3]+","+numpy_seq[i+1][2]+","+numpy_ann[k][1]+","+numpy_ann[k][2]+","+numpy_ann[k][3]+","+numpy_ann[k][4]
                    #print(numpy_seq[i][3],numpy_seq[i+1][2],numpy_ann[k][1],numpy_ann[k][2],numpy_ann[k][3])
                    print(result,file=opf)
                    #print(numpy_seq[i][3],numpy_seq[i][0],numpy_seq[i+1][1],numpy_seq[i+1][2],
                    #      numpy_ann[k][1],numpy_ann[k][2],numpy_ann[k][3])
                    break
#            '''
#############################################################
    
def main(fname):
    import sys
    import os
    import pandas as pd
    import openpyxl
    from numpy import loadtxt

    #pbid="/d/PatBaSe_Project/PatBaSe_Package/patebase_internaldata"
    #pbid = "patebase_internaldata"
    pbid = "../patebase_internaldata"
#    ''' 
#To read row_dev values and position weight matrix
    rws_pwm=pbid+"/positional_weight_factors.csv"
    cIDdRn=fname+"_cIDdRn.csv"
    cIDseq=fname+"_cIDseq.csv"
    print("----->generate_cIDseq file")
    dRn_to_LetterSeq(rws_pwm,cIDdRn,cIDseq)
    
#To read 20x20 weight matrix
    cIDseq = fname+"_cIDseq.csv"
    ref_seqcID = pbid+"/80p_all_reps.csv"
    ref_cID = pbid+"/80p_all_reps_cidsm_annotations.csv"
    pwf = pbid+"/positional_weight_factors.csv"
    wm2 = pbid+"/wm2.csv"
    PScut=85.0
    print("----->Read weight matrix wm2")
    read_refcIDwm2(cIDseq,ref_seqcID,ref_cID,pwf,wm2,PScut)

#To Auto Annotate curves from knowledge base
    queryf = fname+"_yesRelatedReference.csv"
    refannf = pbid+"/80p_rep_cID_annotatedit.csv"
    #refannf=fname+"_annotations.csv"
    cIDdRnf=fname+"_cIDdRn.csv"
    cIDdRnAnn=fname+"_cIDdRnAnn.csv"
    print("----->Assigning annotations to curves similar to reference curves")
    assign_annotation(queryf,refannf,cIDdRnf,cIDdRnAnn)
#    '''
#Move metadata to Meta_DATA folder
    print("----->Transferring meta data files to Meta_DATA folder")
    cIDdRn=fname+"_cIDdRn.csv"

    clean_cIDdRn = "sed 's/\[//g' "+cIDdRn+" | sed 's/\]//g' > "+fname+"_clcIDdRn.csv"
    os.system(clean_cIDdRn)
    f=str(fname)

    get_noRRcID="cut -d' ' -f4 "+f+"_noRelatedReference.csv > "+f+"_noRelatedReference.txt"
    os.system(get_noRRcID)
    os.system("dos2unix "+f+"_noRelatedReference.txt")

    com_move_mf="mv "+fname+"_* Meta_DATA/"
    print(com_move_mf)
    os.system(com_move_mf)

    get_noRR="grep -f Meta_DATA/"+f+"_noRelatedReference.txt Meta_DATA/"+fname+"_clcIDdRn.csv > "+f+"_noRRcIDdRn.csv"
    print(get_noRR)
    os.system(get_noRR)
    
    com_results="mv Meta_DATA/"+fname+"_cIDdRnAnn.csv ."
    print(com_results)
    os.system(com_results)
    #com_results2="mv Meta_DATA/"+fname+"_noRRcIDdRn.csv ."
    
#Execute main() function
if __name__ == '__main__':
    main(fname)
