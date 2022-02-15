from deck import Deck
from hand import Hand
import time

class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        self.deck.create_deck()
        self.deck.shuffle()
        self.player.str_hand.append(self.deck.deal(1))
        self.player.str_hand.append(self.deck.deal(1))
        print(f"You are dealt: {self.player.get_str_hand()}")
        self.dealer.str_hand.append(self.deck.deal(1))
        print(f"The dealer is dealt: {self.dealer.get_str_hand()}, Unknown")
        
        

            