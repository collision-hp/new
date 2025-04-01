class Person:
    name="King"
    def changeName(self,name):
        self.name=name #this creates a new name attribute for object not the class name attribute
p1=Person()
p1.changeName("Virat Kohli")
print(p1.name)#object attribute name changed
print(Person.name)#but Class attribute actual name doesn't change


#SOLUTION

class Person:
    name="King"
    
    #METHOD 1
    # def changeName(self,name):
    #     Person.name=name #this accesses the predefined name attribute for object in the class

    #METHOD 2
    @classmethod
    def changename(cls,name):
        cls=name=name

p1=Person()
p1.changename("Virat Kohli")
print(p1.name)#object attribute name changed
print(Person.name)#Class attribute actual name also changed