class Squaer:
    a=[]
    def __init__(self,x):
        self.x=x
        self.a.append(self.x)

    def __repr__(self):
        return "{} by {}  by {} by {}".format(self.x,self.x,self.x,self.x)


r1=Squaer(29)

print(r1)
