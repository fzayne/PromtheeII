import numpy as np


def combinaison(n,p):
    return int ((np.math.factorial(n))/np.math.factorial(n-p))

def normlizematrix(matrix,critere=None):
    matrix = np.array(matrix,dtype=float)
    max =np.amax(matrix,axis=0)
    min = np.amin(matrix,axis=0)
    # for row in matrix:
    #     print(row)
    # max=matrix.max(axis=0)
    # min=matrix.min(axis=0)
    
    print(f"the maximum is :{max}")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if critere!=None and j in critere:
                matrix[i][j]=(max[j]-matrix[i][j])/(max[j]-min[j])
            else:
                matrix[i][j]=(matrix[i][j]-min[j])/(max[j]-min[j]) 
            
    return matrix


def preferenceMatrix(matrix):
    prefmatrix=np.zeros(shape=(combinaison(len(matrix),2),len(matrix[0])))
    
    it=0
    for i in range(len(matrix)):  
        for j in range(len(matrix)):
            if i!=j:
                for k in range(len(matrix[0])):
                    prefmatrix[it][k]=preferencefunction(i,j,matrix,k)
                
                it+=1
    return prefmatrix


def preferencefunction(a,b,matrix,critere):
    preference=matrix[a][critere]-matrix[b][critere]
    if preference<0:
        preference=0
    return preference

def aggPreference(matrix,weights,nalt):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j]=matrix[i][j]*weights[j]
    
    aggPref=matrix.sum(axis=1)
    
    aggPrefMat=np.zeros(shape=(nalt,nalt))
    
    it=0
    for i in range(nalt):
        for j in range(nalt):
            if i!=j:
                aggPrefMat[i][j]=aggPref[it]
                it+=1
    return aggPrefMat

def flow(aggMat):
    inflow=np.sum(aggMat,axis=0)/(len(aggMat)-1)
    outflow=np.sum(aggMat,axis=1)/(len(aggMat)-1)
    netflow=np.zeros(shape=len(inflow))
    for i in range(len(inflow)):
        netflow[i]=outflow[i]-inflow[i]
    return netflow

def getRank(netflow):
    return np.argsort(-netflow).argsort()

def calculPromtheeII(weights,matrix):
    matrix=np.array(matrix,dtype=float)
    matrix=matrix[:,1:]
    for row in matrix:
        print(row)

    print("========================================================================")
    print(weights)
    
    print(f"mat colmn :{len(matrix[0])}  poids:{len(weights)}")
    nalt=len(matrix)
    matrix=normlizematrix(matrix)
    prefMatrix=preferenceMatrix(matrix)
    aggPrefMatrix=aggPreference(prefMatrix,weights,nalt)
    netflow=flow(aggPrefMatrix)
    rank=getRank(netflow)
    return rank