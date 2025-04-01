class Car:
    brand="Mercedes"
    def __init__(self,model,price):
        self.model=model
        self.price=price
    def get_price(self):
        print("The price of the car is",self.price)
        return "Thank You"
    
car1=Car("XL6",13.5)
print(car1.get_price())






   