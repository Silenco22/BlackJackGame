import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = Card()
        self.num_cards = 52
        self.deck = []

    def create_deck(self):
        self.deck = []
        for i in range(len(self.cards.symbol)):
            for x in range(len(self.cards.value)):
                self.deck.append(self.cards.value[x+1] + self.cards.symbol[i])
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
        

    def deal(self, num_cards):
        for i in range(num_cards):
            return self.deck.pop()

