# importing pandas module
import pandas as pd
import openpyxl
import sys
import os
filename = sys.argv[1]

'''
os.system("rm *t.del")
for i in range(48):
     if i<2:
        continue
     I=str(i-1)
     J=str(i)
     cmd = "cut -d',' -f"+J+" "+filename+" | sort -n -r > t"+I+".del"
     print(cmd)
     os.system(cmd)
     cmd1="awk -v var='Cycle' '$0~var{print NR}' t"+I+".del>>zero_position.del"
     print(cmd1)
     os.system(cmd1)
'''
os.system("rm *t*_*.del")
zp=open('zero_position.txt',"r")
i=1
for cpos in zp:
    #print(cpos)
    ptp=float(cpos)/10.0
    kkk=5737-int(cpos)
    ntp=float(kkk)/10.0
    #print(int(ptp),int(ntp),(5737-int(ntp)))
    #print(int(ptp),(5737-int(ntp)))
    
    s1=str(int(ptp))
    I=str(i)
    cmd01="head -"+s1+" t"+I+".del >> t"+I+"_1.del"
    #print(cmd01)
    os.system(cmd01)
    
    f1="t"+I+"_1.del"
    df1=pd.read_csv(f1,header=None)
    print(df1.sum()/ptp/9.0)
    
    s2=str(int(ntp))
    cmd02="tail -"+s2+" t"+I+".del >> t"+I+"_2.del"
    #print(cmd02)
    os.system(cmd02)

    f2="t"+I+"_2.del"
    df=pd.read_csv(f2,header=None)
    #print(df.sum()/ntp/9.0)

    i += 1
zp.close()

