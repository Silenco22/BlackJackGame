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
    if player.balance > 0:
        start = input(f"You are starting with ${player.balance}. Would you like to play a hand? ")
        if start != "yes":
            print("Game over! Please restart this program to try again.")
            break
        game.start_game()
        player_current_value = sum_of_cards11(player.get_str_hand())
        player_end_value = 0
        card = ""
        decision = ""
        
        while True:
            if player_current_value  == 21:
                player_end_value = 21
                break #its dealers turn

            if player_current_value < 21:
                #msm da tu treba jos nekaj provjeriti zbo vise asoa mozda neam pojma za sad
                decision = dealer.hit()
                if decision == "stay":
                    player_end_value = player_current_value
                    break
                elif decision == "hit":
                    card = game.deck.deal(1)
                    print("You are dealt: ", card)
                    
                    player.str_hand.append(card)
                    print("You now have: ", player.get_str_hand())
                    player_current_value = sum_of_cards11(player.get_str_hand())
                    continue
            if player_current_value > 21:
                if sum_of_card_AA(player.get_str_hand) > 21:
                    if sum_of_cards1(player.get_str_hand) > 21:
                        print(f"Your hand value is over 21 and you lose ${game.bet} :(")
                        player_boolean = True
                        player.balance = player.balance - game.bet
                        break
                    else:
                        player_current_value = sum_of_cards1(player.get_str_hand)
                        continue
                else:
                    player_current_value = sum_of_card_AA(player.get_str_hand)
                    continue

        if player_boolean == False:
            #dealers turn
            dealer.str_hand.append(game.deck.deal(1))
            dealer_current_value = sum_of_cards11(dealer.get_str_hand())
            dealer_end_value = 0
            print("The dealer has: ", dealer.get_str_hand())
            card = ""
            
            while True:
                if dealer_current_value  == 21:
                    dealer_end_value = 21
                    break #its dealers turn

                elif dealer_current_value < 17:
                    card = game.deck.deal(1)
                    dealer.str_hand.append(card)
                    print(f"The dealer hits and is dealt: {card}") 
                    dealer_current_value = sum_of_cards11(dealer.get_str_hand())
                
                elif dealer_current_value >= 17 and dealer_current_value < 21:
                    dealer_end_value = dealer_current_value
                    print("The dealer stays.")
                    break

                elif dealer_current_value > 21:
                    if sum_of_card_AA(dealer.get_str_hand()) > 21:
                        if sum_of_cards1(dealer.get_str_hand()) > 21:
                            print(f"The dealer busts, you win ${game.bet} :)")
                            player.balance = player.balance + game.bet
                            dealer_boolean = True
                            break
                        else:
                            dealer_current_value = sum_of_cards1(dealer.get_str_hand)
                            continue
                    else:
                        dealer_current_value = sum_of_card_AA(dealer.get_str_hand)
                        continue
        if dealer_boolean == False:
            if player_end_value > dealer_end_value:
                print(f"You win ${game.bet} :)")
                player.balance = player.balance + game.bet
            elif player_end_value < dealer_end_value:
                print(f"The dealer wins, you lose ${game.bet} :(")
                player.balance = player.balance - game.bet
            elif player_end_value == dealer_end_value:
                print("You tie. Your bet has been returned.")
    else:
        print("You've ran out of money. Please restart this program to try again. Goodbye.")
        break

                



            
            

















