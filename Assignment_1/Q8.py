class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def display_info(self):
        print(self.make)
        print(self.model)
class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make,model)
        self.num_doors=num_doors
    def display_info(self):
        print(self.num_doors)
        return super().display_info()
v1=Vehicle("Ford","Everest")
v1.display_info()
c1=Car("Ford","Everest",43)
c1.display_info()