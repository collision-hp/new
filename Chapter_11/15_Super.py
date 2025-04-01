class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car stopped")
class Ford(Car):
    def __init__(self,model,type):
        self.model=model
        super().__init__(type)
        super().start()
        
car1=Ford("Mustang","Petrol")
print(car1.type)