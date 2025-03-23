#PRIVATE ATTRIBUTES AND METHODS
# ________________________________

#NORMAL CLASS WITH PUBLIC ATTRIBUTES AND METHODS
class Account:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.accpass=accpass
acc1=Account(234245476587,1234)
print(acc1.accno)
print(acc1.accpass) #we donot want anyone else to view our password we want to privatise it


#PRIVATE LOCAL ATTRIBUTE
class Privateaccount:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.__accpass=accpass
acc1=Privateaccount(354678,675)
print(acc1.__accpass) #we cannot access a private attribute outside the class


class PrivateAcc_within_class:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.__accpass=accpass
    def passreset(self):
        print(self.__accpass)
acc1=PrivateAcc_within_class(34567890,432)
print(acc1.passreset()) #we can access the private attribute inside the class


#PRIVATE GLOBAL ATTRIBUTE AND PRIVATE FUNCTION
class PrivateAttr:
    __name="anonymous"
    def __hello():
        print("Hello Person")
p1=PrivateAttr()
print(p1.__hello)
print(p1.__name)#we cannot access the funtion or global attribute outside the class


class PrivateAccAttr:
    __name="anonymous"
    def __hello(self,name):
        
        self.__name=name
        print("Hello")
    def welcome(self):
        print(self.__name)
        self.__hello("King")
        print(self.__name)
p1=PrivateAccAttr()
print(p1.welcome())



    