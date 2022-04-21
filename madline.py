#Implementation of MADLINE Neural Network for NOR function
import numpy as np
from prettytable import PrettyTable #for dispaly purpose use 'pip install prettytable' for installing package

inp=np.array([[1,1,-1],[1,-1,-1],[-1,1,-1],[-1,-1,1]]) #input vector Bipolar NOR function
n=2                   #number of input nerurons
m=2                 #number of hidden neurons
v=[float(i) for i in input("Weight Vector [v1,v2,. . ...] to output layer: ").strip().split()]
v=np.array(v)
w=[]
for i in range(n):
  print("Enter weight vector comming from input unit : ",i+1)
  w.append([float(i) for i in input().split()])
w=np.array(w)
b=[float(i)  for i in input("Bias to hidden unit:  ").split()]
b=np.array(b)
bo=float(input("Enter the bias for output unit : "))
alp=float(input("Alpha(Learning Rate): "))
Ep=int(input("Enter the maximum number of epochs for training: ")) 
E=0
table=PrettyTable(["E","w11","w12","w21","w22","b1","b2"])
table.add_row([0,w[0,0],w[0,1],w[1,0],w[1,1],b[0],b[1]])
while(E<Ep):
    wold=w.copy()
    print("Data after Epoc ",E+1)
    for x in inp:
        z=np.array([float(0) for i in range(m)])
        zin=np.array([float(0) for i in range(m)])
        for j in range(m):
            s=b[j]
            for i in range(n):
                s+=(x[i]*w[i,j])
            zin[j]=round(s,5)     
        for j in range(m):
            if(zin[j]>=0):
                z[j]=1.0
            else:
                z[j]=-1.0
        yin=bo+np.dot(z,v)
        if(yin>=0):
            y=1
        else:
            y=-1
        #cheking the net activation     
        if(y!=x[-1]):
            indexes=[]
            if(x[-1]==-1): #
                for i in range(m):
                    if(zin[i]>0):
                        indexes.append(i)
            elif(x[-1]==1):
                if(abs(zin[0])==abs(zin[1])):
                    indexes.append(0)
                    indexes.append(1)
                elif(abs(zin[0])<abs(zin[1])):
                    indexes.append(0)
                else:
                    indexes.append(1)
                
            for i in range(n):
                for j in indexes:
                    temp=alp*( x[-1]-zin[j])*x[i]
                    w[i,j]=w[i,j]+temp
            for i in indexes:
                b[i]=b[i]+(alp*(x[-1]-zin[i]))
        #print(w,b)
    
    

    check=w==wold
    table.add_row([E+1,round(w[0,0],3),round(w[0,1],3),round(w[1,0],3),round(w[1,1],3),round(b[0],3),round(b[1],3)])
    if(check.all()):
        print("\n\n")
        print(E+1,"No changes in weight detected Training Completed...!")
        break
    else:
        E+=1
print(table)
