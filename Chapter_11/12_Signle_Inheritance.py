class Car:
    color="White"
    @staticmethod
    def start():
        print("Car start....")
    @staticmethod
    def stop():
        print("Stopped!!!!")
    @staticmethod
    def engine():
        print("Hybrid Engine<>")
        
class Toyota(Car):
    def __init__(self,name):
        self.name=name
        
car1=Toyota("Fortuner")
car2=Toyota("Cruiser")
print(car1.start())
print(car1.color)