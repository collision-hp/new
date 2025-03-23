class Student:
    #parameterized constructer
    def __init__(self,name,redgno):
        self.name=name
        self.redgno=redgno
        print("Printing info of the students")
    
    # #default constructer 
    # def __init__(self):
    #     print("This is default constructer")
    #     pass
    
s1=Student("Elvish",123)
print(s1.name)
s2=Student("Yadhav",542)
print(s2.name)
print(s1.redgno)

# s3=Student()
# print(s3)