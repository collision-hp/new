#Create account class with two attributes -balance and account no.
#Create method for debit,credit and printing the balance

class Account:
    def __init__(self,bal,accno):
        self.bal=bal
        self.accno=accno
    def debit(self):
        rs=int(input("Enter amount to be debited"))
        self.bal-=rs
        print(self.bal)
    def credit(self):
        rp=int(input("Enter amount to be credited"))
        self.bal+=rp
        print(self.bal)
    def pb(self):
        print("You are left with ",self.bal)

acc1=Account(10000,5436787890678)
acc1.debit()
acc1.credit()
acc1.pb()
