from os import system
import random
from Day11_art import logo
# Day 11 Capstone project
def choice_for_Ace():
    print("You've got an Ace")
    return int(input("What should it's value be? 1 or 11?: "))
    
card_val = {
    'A':11,
    'K':10,
    'Q':10,
    'J':10
}

def get_card_val(card):
    if card in card_val:
        return card_val[card]
    else:
        return card
    
def blackjack():
    '''
    Call this function to start a blackjack game. It uses the logo from Day11_art module for logo
    If you don't want the logo just comment or put your own art in it
    '''
    while True:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() != 'y':
            return
        system('cls')
        cards = [i for i in range(1,11)]*4
        cards += ['A']*4 + ['Q']*4 + ['K']*4 + ['J']*4
        random.shuffle(cards)
        card_val['A'] = 11
        print(logo)
        player_continue = True
        user_cards = [cards.pop(), cards.pop()]
        user_cards_val = sum([get_card_val(card) for card in user_cards])
        
        computer_cards = [cards.pop()]
        computer_cards_val = get_card_val(computer_cards[0])
        card_val['A'] = 1
        while user_cards_val<21 and computer_cards_val<17:
            print(f"Your cards: {user_cards}, current score: {user_cards_val}")
            print(f"Computer's cards: {computer_cards}, current score: {computer_cards_val}")
            
            
            if player_continue and input("Type 'y' to get another card, type 'n' to pass: ") != 'y':
                player_continue =  False
        
            if player_continue:
                next_card = cards.pop()
                user_cards.append(next_card)
                if next_card == 'A':
                    if user_cards_val + 11 > 21:
                        user_cards_val += 11
                    else:
                        user_cards_val += choice_for_Ace()    
                else:
                    user_cards_val += get_card_val(next_card)
            next_card = cards.pop()
            computer_cards.append(next_card)
            if next_card == 'A':
                if computer_cards_val + 11 > 21:
                    computer_cards_val += 11
                else:
                    computer_cards_val += 1
            else:
                computer_cards_val += get_card_val(next_card)
        
        print(f"Your final hand: {user_cards}, current score: {user_cards_val}")
        print(f"Computer's final card: {computer_cards}, current score: {computer_cards_val}")
        if user_cards_val > 21:
            print("You Lose! 😭")
        elif computer_cards_val > 21:
            print("You Win! 😁")
        elif user_cards_val == computer_cards_val:
            print("Draw! 😮")
        elif computer_cards_val < user_cards_val:
            print("You Win! 😁")
        else:
            print("You Lose! 😭")
     
blackjack()