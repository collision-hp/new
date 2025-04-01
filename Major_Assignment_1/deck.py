import random
from cards import Card

class Deck:
    def __init__(self):
        self.cards = [Card(face, suit) for suit in Card.suits for face in Card.faces]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:] #line updates the self.cards list by removing the first num_cards elements
        return dealt_cards

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)