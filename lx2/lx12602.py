class Circle():
    def __init__(self,a):
        self.width=a
    def area(self):
        import math
        
        return math.pi*self.width*self.width

cf1=Circle(5)
print(cf1.area())
