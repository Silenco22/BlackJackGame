def sum_of_cards11(lst):
    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K"
    }
    card_values_lst = []
    for card in lst:
        for key in range(len(VALUE_NAMES)):
            if card[0] == VALUE_NAMES.get(key + 1):
                if card[0] == "A":
                    card_values_lst.append(11) #gives 11 value for card 'A'
                    break
                elif key + 1 < 10:
                    card_values_lst.append(key + 1)
                    break
                else:
                    card_values_lst.append(10) #gives 10 value for any face card
                    break

    return sum(card_values_lst)

def sum_of_cards1(lst):
    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K"
    }
    card_values_lst = []
    for card in lst:
        for key in range(len(VALUE_NAMES)):
            if card[0] == VALUE_NAMES.get(key + 1):
                if key + 1 < 10:
                    card_values_lst.append(key + 1)
                    break
                else:
                    card_values_lst.append(10) #gives 10 value for any face card
                    break

    return sum(card_values_lst)

def sum_of_card_AA(lst):
    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K"
    }
    card_values_lst = []
    counter = 0
    for card in lst:
        for key in range(len(VALUE_NAMES)):
            if card[0] == VALUE_NAMES.get(key + 1):
                if card[0] == "A":
                    if counter == 0:
                        card_values_lst.append(11)
                        counter += 1
                        #gives 11 value for card 'A'
                        break
                    else:
                        card_values_lst.append(1)
                        break
                elif key + 1 < 10:
                    card_values_lst.append(key + 1)
                    break
                else:
                    card_values_lst.append(10) #gives 10 value for any face card
                    break

    return sum(card_values_lst)


lst = ["23","Q2","T5"]
print(sum_of_card_AA(lst))