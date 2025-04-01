class Employee:
    def __init__(self,role,sal,dept):
        self.role=role
        self.sal=sal
        self.dept=dept
    def display(self):
        print("Role ",self.role)
        print("Salary ",self.sal)
        print("Department ",self.dept)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","21","1500000")
e1=Employee("Software Developer","1500000","Technical")
e1.display()
eng1=Engineer("Mark Zukerberg",45)
eng1.display()