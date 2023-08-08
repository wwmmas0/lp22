class Horse():
    def __init__(self,a,b,c,d):
        self.high=a
        self.weight=b
        self.collor=c
        self.owner=d


class Rider():
    def __init__(self,name):
        self.name=name


l=Rider("Jake")
m=Horse(76,230,"yellow",l)
print(m.owner.name)
