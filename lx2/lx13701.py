class Shape():
    def what_am_i(self):
        print("I am s shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width=w
        self.len=l

    def calculate_perimeter(self):
        return self.width*2+self.len*2


class Square(Shape):
    def __init__(self,l):
        self.len=l

    def calculate_perimeter(self):
        return self.len*4
    def change_size(self,l):
        self.len=self.len+l



r=Rectangle(5,6)
s=Square(9)

print("长方形周长：{}".format(r.calculate_perimeter()))
r.what_am_i()

print("正方形周长：{}".format(s.calculate_perimeter()))
s.what_am_i()
s.change_size(-1)
print("正方形边长减1的周长：{}".format(s.calculate_perimeter()))









