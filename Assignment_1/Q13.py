class balExep(Exception):
    def __init__(self,balance,withdraw):
        self.balance=balance
        self.withdraw=withdraw
    def __str__(self):
        return f"Insufficient balance {self.balance} but withdrawal amounnt is {self.withdraw}"

class BankAccount:
    def __init__(self,bal):
        self.bal=bal
    def withdraw(self,amt):
        if amt>self.bal:
            raise balExep(self.bal,amt)
        self.bal-=amt
        return self.bal
if __name__=="__main__":
    acc=BankAccount(1000)
    try:
        print("Current Balance is ",acc.bal)
        acc.withdraw(5000)
    except balExep as e:
        print("Error:",e)
        