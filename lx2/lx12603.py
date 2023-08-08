class Triangle():
    def __init__(self,a,b):
        self.width=a
        self.len=b
    def area(self):
        
        return self.width*self.len

cf1=Triangle(5,9)
print(cf1.area())
