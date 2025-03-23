from deck import Deck
from player import Player
def main():
    deck=Deck()
    p1=Player("Alice")
    p2=Player("Sophie")
    p1.receive(deck.deal(5))
    p2.receive(deck.deal(5))

    print(p1)
    print(p2)

main()
