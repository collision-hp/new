import math
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return self.rad**2 * math.pi
class Rectangle(Shape):
    def __init__(self,len,bread):
        self.len=len
        self.bread=bread
    def area(self):
        return self.len*self.bread

c1=Circle(2)
print(c1.area())
r1=Rectangle(2,3)
print(r1.area())