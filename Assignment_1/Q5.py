class Time:
    def __init__(self,timefrmt):
        self.timefrmt=timefrmt
        self.hh=0
        self.mm=0
        self.ss=0

    def conv(self):
        if(self.timefrmt>12):
            print(self.timefrmt-12)
    def valid(self):
        if(self.hh>24 or self.hh<00 or self.mm>60 or self.mm<00 or self.ss>60 or self.ss<00 or ":" not in self.timefrmt[2] or ":" not in self.timefrmt[5]):
            print()
    