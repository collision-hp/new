class Card:
    faces=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    suits=['Hearts','Diamonds','Clubs','Spades']
    def __init__(self,face,suit):
        self.face=face
        self.suit=suit
    # method __repr__ returns a string representation
    def __repr__(self):
        return f"Card(f={self.face},s={self.suit})"

    # Method __str__ returns a string of the format 'face of suit', such as 'Ace of Hearts'
    def __str__(self):
        return f"{self.face}of{self.suit}"
    
    #  method __format__ is called when a Card object is formatted as a string, such as in an f-string:
    def __format__(self,format):
        return f"{str(self):{format}}"


