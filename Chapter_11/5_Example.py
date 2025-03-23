#to calculate average of the marks of 3 students
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self,s1,s2,s3):
        return (s1.marks+s2.marks+s3.marks)/3
s1=Student("Virat",152)
s2=Student("Rohit",221)
s3=Student("Gill",31)
print(s1.avg(s1,s2,s3))