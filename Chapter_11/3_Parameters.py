class Student:
    college="Iter"
    name="Anonymous"#class attributes
    def __init__(self,name,marks): #object attribute
        self.name=name
        self.marks=marks
s1=Student("King",18)
s2=Student("ABD",17)
print(s1.name)#object attribute has higher precedence than class attribute
print(s2.marks)

#college name
print(s1.college)
print(s2.college)

#otherwise directly
print(Student.college) #for class attribute
print(Student.name)