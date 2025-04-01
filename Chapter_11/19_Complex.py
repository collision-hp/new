#Normal Method
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def display(self):
        print(self.real," + ",self.imag,"j")
    def add(self,num2):
        newReal=self.real+num2.real
        newImag=self.imag+num2.imag
        return Complex(newReal,newImag)
num1=Complex(2,3)
num1.display()

num2=Complex(4,5)
num2.display()

num3=num1.add(num2)
num3.display()

print("Using Dunder Function from polymorphism<------------------->")
#Dunder Function
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def display(self):
        print(self.real," + ",self.imag,"j")
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImag=self.imag+num2.imag
        return Complex(newReal,newImag)
    
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImag=self.imag-num2.imag
        return Complex(newReal,newImag)

num1=Complex(2,3)
num1.display()

num2=Complex(4,5)
num2.display()

num3=num1+num2
num3.display()

num4=num2-num1
num4.display()