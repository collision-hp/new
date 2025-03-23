class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    #user-defined Dunder Function
    def __gt__(self,ord2):
        return self.price>ord2.price
ord1=Order("Chips",10)
ord2=Order('Ice Cream',40)
print(ord1>ord2)
        
        