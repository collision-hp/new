class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    @staticmethod
    def hello():
        print("Hello")
s1=Student("Gill",321)
s1.hello()
print(s1.name)