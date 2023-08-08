class abc:
    def __init__(self,a):
        self.a=a


r1=abc("Jak")

r2=abc("Tom")
r3=r1
print(r1 is r2)
print(r1 is r3)
