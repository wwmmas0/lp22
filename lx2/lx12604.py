class Hexagon():
    def __init__(self,a):
        self.width=a
    def area(self):
        import math
        
        return math.pi*self.width*2

cf1=Hexagon(5)
print(cf1.area())
