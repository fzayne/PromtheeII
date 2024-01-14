

def score(poids,ranks,DecideurNum):
    sc=0.0
    for i in range(DecideurNum):
        sc=poids[i]*ranks[i]+sc
    return sc

def column(matrix, i):
    return [row[i] for row in matrix]

def scorage(totalWeights,totalRank,ActionNum,DecideurNum):
    poids=column(totalWeights,0)
    print(poids)
            
