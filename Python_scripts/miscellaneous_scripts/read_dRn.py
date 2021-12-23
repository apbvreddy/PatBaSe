f = open("dRn.csv", "r")
f.readline()
i = int()
drn=[10.0,20.0,20.0]
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
        drn[j]=float(y[5])
    else:
        drn.append(float(y[5]))
    i+=1
    j+=1
    if (i==46):
        print(drn)
        i=0
        #break
        
f.close()
