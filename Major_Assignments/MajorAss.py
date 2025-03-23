import random
from enum import Enum
class Suit(Enum):
    HEARTS="Hearts"
    DIAMONDS="Diamonds"
    CLUBS="Clubs"
    SPADES="Spades"

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    rank=["Ace",'2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    
    def __repr__(self):
        return f"Card(r={self.rank},s={self.suit})"

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards=[Card(suit,rank) for suit in Suit for rank in Card.rank]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self,no):
        dealt=self.cards[:no]
        self.cards=self.cards[no:]
        return dealt
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
class Player():
    def __init__(self,name):
        self.name=name
        self.hand=[]
    def receive(self,cards):
        self.hand.extend(cards)
    def show(self):
        return ', '.join(str(card) for card in self.hand)
    def __str__(self):
        return f"Player {self.name} has {self.show()}"
    def calcsc(self):
        score = 0
        aces = 0
        for card in self.hand:
            if card.rank in ['Jack', 'Queen', 'King']:
                score += 10
            elif card.rank == 'Ace':
                aces += 1
                score += 11
            else:
                score += int(card.rank)
        
        while score > 21 and aces:
            score -= 10
            aces -= 1
        
        return score
def blackjack():
    deck = Deck()
    players = [Player("Player 1"), Player("Player 2")]
    dealer = Player("Dealer")

    # Initial deal
    for player in players:
        player.receive(deck.draw(2))
    dealer.receive(deck.draw(2))

    for player in players:
        print(player)
        print(f"{player.name}'s score: {player.calcsc()}")
    print(dealer)
    print(f"Dealer's score: {dealer.calcsc()}")

    # Players' turns
    for player in players:
        while player.calcsc() < 21:
            action = input(f"{player.name}, do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                player.receive(deck.draw(1))
                print(player)
                print(f"{player.name}'s score: {player.calcsc()}")
            elif action == 's':
                break

        if player.calcsc() > 21:
            print(f"{player.name} busts!")

    # Dealer's turn
    while dealer.calcsc() < 17:
        dealer.receive(deck.draw(1))
        print(dealer)
        print(f"Dealer's score: {dealer.calcsc()}")

    if dealer.calcsc() > 21:
        print("Dealer busts! Remaining players win.")
        return

    # Determine winners
    for player in players:
        if player.calcsc() <= 21:
            if player.calcsc() > dealer.calcsc():
                print(f"{player.name} wins!")
            elif player.calcsc() < dealer.calcsc():
                print(f"{player.name} loses!")
            else:
                print(f"{player.name} ties with the dealer!")

if __name__ == "__main__":
    blackjack()
# point={["King","Queen","Jack"]:10,
#         "Aces":1,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}


        
