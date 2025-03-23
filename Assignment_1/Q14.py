import random
class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def __init__(self,suits,faces):
        self.suits=suits
        self.faces=faces
    def __repr__(self):
        return f"Cards({self.suits},{self.faces})"
    def __str__(self):
        return f'{self.suits}of{self.faces}'
class Deck:
    def __init__(self):
        self.cards=[Card(suits,faces) for suits in Card.suits for faces in Card.faces]
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self,no):
        dealt=self.cards[:no]
        self.cards=self.cards[no:]
        return dealt
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
    
class Player(Deck):
    def __init__(self,name):
        self.name=name
        self.hand=[]
    def hold(self,cards):
        self.hand.append(cards)
    def show(self):
        return ", ".join(str(cards) for cards in self.hand)
    def __str__(self):
        return f'Player {self.name} has {self.show()} cards'

class Main:
    p1=Player("Alice")
    p2=Player("Perry")
    d1=Deck
    p1.hold(Deck().deal(5))
    p2.hold(Deck().deal(5))
    print(p1)
    print(p2)
    
if __name__=="__main__":
    Main
    
