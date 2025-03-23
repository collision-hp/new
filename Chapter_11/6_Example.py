#to calculate average for the list of marks of a student
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("The average marks of the student is ",sum/3)
s1=Student("King",[12,13,14])
s1.average()




