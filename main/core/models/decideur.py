from core.promtheeII import calculPromtheeII
from core.readJson import readJson

class Decideur:
    
    def __init__(self,decideurName,poids):
        self.action=[]
        self.name=decideurName
        self.subjectiveParametre,self.categories=readJson(decideurName)
        self.weights=[row[0] for row in self.subjectiveParametre]
        self.rank=[]
        self.poid=poids

    def calculatePromethee(self,performanceMatrix):
        self.rank= calculPromtheeII(self.weights,performanceMatrix)
        