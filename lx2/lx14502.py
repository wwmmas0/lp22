class Squaer:
    a=[]
    def __init__(self,x):
        self.x=x
        self.a.append(self.x)

    def print_size(self):
        print("""{} by {}  by {} by {}""".format(self.x,self.x,self.x,self.x))


r1=Squaer(29)

r1.print_size()
