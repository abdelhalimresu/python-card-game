from deck import Deck


class Hand(Deck):

    def __init__(self, label):
        self.cards = []
        self.label = label
        self.win_count = 0

    def get_win_count(self):
        return self.win_count

    def round_winner(self):
        self.win_count += 1

    def __str__(self):
        return self.label + super().__str__()
