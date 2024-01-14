class Initiateur:
    def __init__(self) :
        self.performanceMatrix=[]
        self.actions=[]
        self.critere=[]
        self.score=[]
    
    def calculateScorage(self,decideurs):
        self.score=[]
        for i in range(len(self.actions)):
            sc=0
            for decideur in decideurs:
                sc=decideur.poid*decideur.rank[i]+sc
            self.score.append(sc)
        print("=========================================================================================")
        print("score")
        print(self.score)

        
