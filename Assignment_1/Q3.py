class Chapters:
    def __init__(self,title,page):
        self.title=title
        self.page=page
        
class Book:
    def __init__(self,chap):
        self.chap=chap
    def tot(self):
        for i in self.chap:
            print(f"{i.title} : {i.page}")
        return sum(i.page for i in self.chap)
    
c1=Chapters("DFGHJK",12)
c2=Chapters("DFijK",10)
c3=Chapters("tyhj",15)
b1=Book([c1,c2,c3])
print(b1.tot())



