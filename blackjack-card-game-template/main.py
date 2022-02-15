import time
from player import Player
from dealer import Dealer
from game import Game
from sum_of_cards import sum_of_cards1, sum_of_cards11, sum_of_card_AA

STARTING_BALANCE = 500
player = Player(STARTING_BALANCE)
dealer = Dealer()
game = Game(player, dealer)

player_boolean = False
dealer_boolean = False


print("Welcome to Blackjack!")
print()
while True:
    time.sleep(0.5)
    if player.balance > 0:
        player.str_hand =  []
        dealer.str_hand = []
        start = input(f"You are starting with ${player.balance}. Would you like to play a hand? (yes or no) ")
        if start == "no":
            print("Game will end in 5 seconds!")
            x = 5
            for i in range(5):
                time.sleep(1)
                print(f"{x}...")
                x -= 1
            break
        if start != "yes":
            time.sleep(0.5)
            print("Valid input is 'yes' or 'no'. Try again ")
            time.sleep(1)
            continue
        
        while True:
            game.bet = int(input("Place your bet: "))
            if game.bet < Game.MINIMUM_BET:
                print("The minimum bet is $1.")
            elif game.bet > player.balance:
                print(f"The maximum bet is ${player.balance}.")
            else:
                break
        print("Dealing cards")
        time.sleep(1)
        print(".")      
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        # for i in range(3):
        #     print(".", end=" ")
        #     time.sleep(1)
            
        
        game.start_game()
        print()
        player_current_value = sum_of_cards11(player.get_str_hand())
        player_end_value = 0
        card = ""
        decision = ""
        
        while True:
            if player_current_value  == 21:
                player_end_value = 21
                break #its dealers turn

            if player_current_value < 21:
                decision = dealer.hit()
                if decision == "stay":
                    player_end_value = player_current_value
                    break
                elif decision == "hit":
                    card = game.deck.deal(1)
                    time.sleep(1.5)
                    print("You are dealt: ", card)
                    time.sleep(1.5)
                    player.str_hand.append(card)
                    print("You now have: ", player.get_str_hand())
                    time.sleep(1.5)
                    player_current_value = sum_of_cards11(player.get_str_hand())
                    continue
            if player_current_value > 21:
                if sum_of_card_AA(player.get_str_hand()) > 21:
                    if sum_of_cards1(player.get_str_hand()) > 21:
                        print(f"Your hand value is over 21 and you lose ${game.bet} :(")
                        print()
                        time.sleep(1.5)
                        player_boolean = True
                        player.balance = player.balance - game.bet
                        break
                    else:
                        player_current_value = sum_of_cards1(player.get_str_hand())
                        continue
                else:
                    player_current_value = sum_of_card_AA(player.get_str_hand())
                    continue

        if player_boolean == False:
            #dealers turn
            dealer.str_hand.append(game.deck.deal(1))
            dealer_current_value = sum_of_cards11(dealer.get_str_hand())
            dealer_end_value = 0
            print("The dealer has: ", dealer.get_str_hand())
            card = ""
            
            
            while True:
                if len(player.str_hand) == 2 and player_end_value == 21:
                    dealer_end_value = dealer_current_value
                    break
                elif dealer_current_value  == 21:
                    dealer_end_value = 21
                    break 

                elif dealer_current_value < 17:
                    card = game.deck.deal(1)
                    dealer.str_hand.append(card)
                    time.sleep(1.5)
                    print(f"The dealer hits and is dealt: {card}")
                    time.sleep(1.5)
                    print(f"The dealer has: {dealer.get_str_hand()}")
                    time.sleep(1.5)
                    dealer_current_value = sum_of_cards11(dealer.get_str_hand())
                
                elif dealer_current_value >= 17 and dealer_current_value < 21:
                    dealer_end_value = dealer_current_value
                    print("The dealer stays.")
                    time.sleep(1.5)
                    break

                elif dealer_current_value > 21:
                    if sum_of_card_AA(dealer.get_str_hand()) > 21:
                        if sum_of_cards1(dealer.get_str_hand()) > 21:
                            print(f"The dealer busts, you win ${game.bet} :)")
                            player.balance = player.balance + game.bet
                            dealer_boolean = True
                            break
                        else:
                            dealer_current_value = sum_of_cards1(dealer.get_str_hand())
                            continue
                    else:
                        dealer_current_value = sum_of_card_AA(dealer.get_str_hand())
                        continue
            if dealer_boolean == False:
                if len(player.str_hand) == 2 and player_end_value == 21 and dealer_end_value < 21:
                    print(f"Blackjack, You win ${game.bet * 1.5} :)")
                    player.balance = player.balance + game.bet * 1.5
                elif player_end_value > dealer_end_value:
                    print(f"You win ${game.bet} :)")
                    player.balance = player.balance + game.bet
                elif player_end_value < dealer_end_value:
                    print(f"The dealer wins, you lose ${game.bet} :(")
                    player.balance = player.balance - game.bet
                elif player_end_value == dealer_end_value:
                    print("You tie. Your bet has been returned.")
    else:
        print("You've ran out of money. Please restart this program to try again. Goodbye.")
        time.sleep(1)

        print("Game will end in 5 seconds!")
        x = 5
        for i in range(5):
            time.sleep(1)
            print(f"{x}...")
            x -= 1
        
        break

                



            
            

















