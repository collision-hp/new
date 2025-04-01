class AutoMobile:
    @staticmethod
    def engine():
        print("Engine build in Tata Industry pvt. ltd.")
    @staticmethod
    def parts():
        print("Parts are 100% made in India")
class TATA(AutoMobile):
    def __init__(self,brand):
        self.brand=brand
class Curvv(TATA):
    def __init__(self,type):
        self.model=type
    
car1=Curvv("Electric")
car1.engine()
