import random as rn
import matplotlib.pyplot as plt

Population=[]
NumberOfPopulation=100
NumberOfGeneration=2000
allInputFile=[]
FitnessArray=[]
Roulette=[]
 
def generatePopulation(Degree):
    Population.clear()
    for i in range(NumberOfPopulation):
        chromosome=[]
        for j in range(Degree+1):
            chromosome.append(round(rn.uniform(-10, 10), 2))
        Population.append(chromosome)

def readFile():
    listFile=[]
    listFile.clear()
    f=open("input-2.txt", "r")
    for i in f:
        string=i.strip("\n")
        listFile.append(string.split())
    
    f.close()
    return listFile

allInputFile=(readFile())

def getCost(rowPop, rowFile, Degree):
    Y_calc=0
    X=float(allInputFile[rowFile][0])
    for i in range(1,Degree+1):
        Y_calc+=((Population[rowPop][i])*pow(X,i))
    Y_calc+=Population[rowPop][0]
    Y_actual=float(allInputFile[rowFile][1])
    return pow((Y_calc - Y_actual),2)

def getFitness(rowPop, Degree, N):
    cost=0.0
    for i in range(N):
        cost+=getCost(rowPop, i, Degree)
    return cost/N




def fillFitnessArray(Degree, N):
    FitnessArray.clear()
    for i in range(NumberOfPopulation):
        FitnessArray.append(getFitness(i, Degree, N))
        
def selection(Degree, N):
    Roulette.clear()
    fillFitnessArray(Degree, N)
    MaxNumber=max(FitnessArray)*2
    NewFitnessArray=[MaxNumber-x for x in  FitnessArray]
    Total=0
    for x in NewFitnessArray:
        Total+=x 
    for i in range(NumberOfPopulation):
       if i ==0:Roulette.append(NewFitnessArray[i]/Total)
       else:Roulette.append(NewFitnessArray[i]/Total+Roulette[i-1])
    R=rn.uniform(0,1)
    for i in range(NumberOfPopulation):
        if R <=Roulette[i]:return i
    else:return -1

def crossOver(indx1, indx2, Degree):
    R=rn.uniform(0,1)
    if R<0.07:
        R2=rn.randint(0,Degree)
        for i in range(R2,Degree):
            Population[indx1][i], Population[indx2][i]=Population[indx2][i], Population[indx1][i]

def mutation(Poprow, Degree, t,T):
    LB=-10
    UB= 10
    
    for i in range(Degree+1):
        Dl=Population[Poprow][i]-LB
        DU=UB-Population[Poprow][i]
        R1=rn.uniform(0,1)
        if R1<=0.5:y=Dl
        else:y=DU
        r=rn.uniform(0,1)
        b=rn.randint(1,5)
        Delta=y*(1-pow(r,((1-t)/T)**b))
        if y==Dl:
            Population[Poprow][i]=Population[Poprow][i]-Delta
        else:
            Population[Poprow][i]=Delta-Population[Poprow][i]

    
    
def getPoints(N):
    X=[]
    Y=[]
    X.clear()
    Y.clear()
    for i in range(N):
        X.append(float(allInputFile[i][0]))
        Y.append(float(allInputFile[i][1]))
    return X,Y

def calcNew_Y(X, coeff):
    Y=[]
    Y.clear()
    for j in range(len(X)):
        Y_calc=0
        for i in range(1,len(coeff)):
            Y_calc+=(coeff[i] * pow(X[j],i))
        Y_calc+=coeff[0]
        Y.append(Y_calc)
    return Y


def main():
    
    M=int(allInputFile[0][0])
    allInputFile.remove(allInputFile[0])
    
    f=open("output.txt", "w")
    X=[]
    Y=[]
    for case in range(M):
        X.clear()
        Y.clear()
        N=int(allInputFile[0][0])
        Degree=int(allInputFile[0][1])
        allInputFile.remove(allInputFile[0])
        generatePopulation(Degree)
        
        for Generation in range(NumberOfGeneration):
            parent_1=selection(Degree, N)
            parent_2=selection(Degree, N)
            crossOver(parent_1, parent_2, Degree)
            mutation(parent_1, Degree, Generation,NumberOfGeneration)
            mutation(parent_2, Degree, Generation,NumberOfGeneration)
        fillFitnessArray(Degree, N)
        Min=min(FitnessArray)
        for i in range(len(FitnessArray)):
            if FitnessArray[i]==Min:
                indexOfmin=i
                break
        
        X,Y=getPoints(N)
        predicted_Y=calcNew_Y(X, Population[indexOfmin])
        plt.figure()
        plt.scatter(X, Y, color = 'red')
        print("\n")
        plt.plot(X,predicted_Y, color = 'blue')
        f.write("\nCase: ")
        f.write(str(case+1))
        f.write("\n"+str(Population[indexOfmin]))
        
        print("Case: " , case+1, Population[indexOfmin])
        allInputFile[:N]=[]
        FitnessArray.clear()            
  


          
main() 
print("DONE")
