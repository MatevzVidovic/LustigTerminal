

import random as rd


def random_shuffle(input_list):
    examining_list = input_list.copy()
    returning_list = list()

    for i in range(len(input_list)):
        assigned_ix = rd.randint(0, len(examining_list)-1)
        returning_list.append(examining_list[assigned_ix])
        examining_list.pop(assigned_ix)
    return returning_list





suit_dict = {
    1 : 'C',
    2 : 'S',
    3 : 'H',
    4 : 'D'
}

number_dict = {
    7 : '7',
    8 : '8',
    9 : '9',
    10 : '10',
    11 : 'J',
    12 : 'Q',
    13 : 'K',
    14 : 'A'
}


deck = list()
for i in range(7, 15):
    for j in range(1, 5):
        deck.append((i, j))

deck = random_shuffle(deck)

print(deck)

computers_hand = list()
players_hand = list()

def refill_hands(computers_hand, players_hand, deck):
    while(len(deck) > 0 and len(players_hand) < 4):
        computers_hand.append(deck.pop(0))
        players_hand.append(deck.pop(0))
    return

refill_hands(computers_hand, players_hand, deck)

print(players_hand)

def hand_print(hand):
    for i in hand:
        print(number_dict[i[0]] + suit_dict[i[1]], end=" ")
    print()
    return

hand_print(players_hand)










is_player_starting_turn = True
round_stack = list()
is_player_owning_turn = True

player_gottern_cards = list()
computer_gotten_cards = list()

# currently a dummy function
def computer_play(computers_hand, round_stack, is_player_owning_turn):
    round_stack.append(computers_hand[0])
    if (round_stack[0][0] == computers_hand[0][0]):
        is_player_owning_turn = False
    computers_hand.pop(0)
    return is_player_owning_turn


def play_round(computers_hand, players_hand, round_stack):
    
    hand_print(players_hand)

    print("Comp hand for testing:")
    hand_print(computers_hand)

    if(is_player_starting_turn):
        chosen_card = -1
        while(chosen_card < 1 or chosen_card > 4):
            try:
                chosen_card = int(input())
            except:
                print("Please enter a number")
                chosen_card = -1

            if (chosen_card < 1 or chosen_card > 4):
                print("Please enter a number from 1 to 4, 1 being the leftmost number.")
        
        chosen_index = chosen_card -1
        round_stack.append(players_hand[chosen_index])
        players_hand.pop(chosen_index)
        is_player_owning_turn = True

        is_player_owning_turn = computer_play(computers_hand, round_stack, is_player_owning_turn)



        if (is_player_owning_turn):
            player_gottern_cards.extend(round_stack)
        else:
            computer_gotten_cards.extend(round_stack)

    return



play_round(computers_hand, players_hand, round_stack)

print(player_gottern_cards)
print(computer_gotten_cards)
