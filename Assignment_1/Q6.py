class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self):
        amt=int(input("Enter the amount you want to deposit"))
        self.__balance+=amt
        print(self.__balance)
    def withdraw(self):
        draw=int(input("Enter the amount you want to withdraw"))
        self.__balance-=draw
        print(self.__balance)
b1=BankAccount(1000)
b1.deposit()
b1.withdraw()

#They are not accessible by the object directly
#Ensures privacy
