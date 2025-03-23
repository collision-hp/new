import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def __init__(self,suits,values):
        self.suits=suits
        self.values=values
    def __repr__(self):
        return f'Card(f={self.values},s={self.suits})'
    def __str__(self):
        return f'{self.values}of{self.suits}'
    def __format__(self, format_spec):
        return f'{str(self):{format_spec}}'
class Deck(Card):
    def __init__(self):
        self.cards=[Card(suit,values) for suit in self.suits for values in self.values]
        self.suffle()
        
    def suffle(self):
        random.shuffle(self.cards)
    def deal(self,no):
        dealt=self.cards[:no]
        self.cards=self.cards[no:]
        return dealt
    def __str__(self):
        return ', '.join(str(i) for i in self.cards)
            
class Player(Deck):
    def __init__(self,pname):
        self.pno=pname
        self.hand=[]
    def receive(self,cards):
        self.hand.append(cards)
    def show(self):
        return ", ".join(str(card) for card in self.hand)
    def __str__(self):
        return f"Player {self.pno} has {self.show()}"
    
class Main():
    p1=Player("Carry")
    p2=Player("Jonny")
    d1=Deck()
    p1.receive(Deck().deal(5))
    p2.receive(Deck().deal(5))
    print(p1)
    print(p2)
    print(d1)
    
Main()
    