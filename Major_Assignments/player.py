class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
    def receive(self,cards):
        self.hand.append(cards)
    def show(self):
        return ', '.join(str(card) for card in self.hand)
    def __str__(self):
        return f'Player {self.name} has:{self.show()}'
        