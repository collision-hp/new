class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3) + "%"
student1=Student(98,67,23)
print(student1.percentage)
#if we want to update the marks 
student1.phy=78
#situations where we cannot give fixed values to attribute
print(student1.phy)
print(student1.percentage)
#here the value doesn't change

print("After correction<---------------------------------->")
#TO CORRECT THIS
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
    @property
    def percentage(self):
            return str((self.phy+self.chem+self.math)/3) + "%"
student1=Student(98,67,23)
print(student1.percentage)
#if we want to update the marks 
student1.phy=78
#situations where we cannot give fixed values to attribute
print(student1.phy)
print(student1.percentage)