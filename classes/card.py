class Card:
    
    suits = ['♣', '♦', '♥', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.suits[self.suit] + self.ranks[self.rank]

    def __lt__(self, other):
        if self.suit != other.suit:
            return self.suit < other.suit
        return self.rank < other.rank
