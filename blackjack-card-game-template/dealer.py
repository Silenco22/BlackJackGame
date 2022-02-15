class Dealer:
    def __init__(self):
        self.str_hand = []

    def get_str_hand(self):
        return self.str_hand

    def hit(self):
        while True:
            decison = input("Would you like to hit or stay? ")
            if decison != "hit" and decison != "stay":
                print("That is not a valid option.")
            return decison 
