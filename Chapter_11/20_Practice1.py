#Define a Circle class to create a circle with radius r using the constructer
#Define an Area() method of the class which calculates the area of the circle
#Define a Perimeter() method of the class which allows yout to calculate the perimeter of the circle

class Circle:
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return 3.14*self.rad**2
    def peri(self):
        return 2*3.14*self.rad**2
     
c1=Circle(17)
print(c1.area())
print(c1.peri())