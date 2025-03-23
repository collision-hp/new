class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def display(self):
        print(self.real,"+",self.imag,"j")
    def add(self,num2):
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return Complex(newreal,newimag)
num1=Complex(2,3)
num2=Complex(4,5)
num1.display()
num2.display()
num1.add(num2).display()
