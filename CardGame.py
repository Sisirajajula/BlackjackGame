from art import logo
import random
# choose from deck of cards and calculate the sum of cards.
# Jack, Queen, King cards are counted as 10
# Ace is counted as 11
# Normally if a card is drawn,probability of getting the same card again gets decreased.
# Here, it is assumed that all cards have same probability of getting drawn.
def deal_cards(Cards,n):
    if n == 2:
        cards_drawn = random.choices(Cards,k=n)
    elif n == 1:
        cards_drawn = random.choice(Cards)
    return cards_drawn
def display(User,computer):
        print("Your cards: {}, Final score: {}".format(User,sum(User)))
        print("Computer's Final hand {}, Final score: {}".format(computer,sum(computer)))
def result(User,computer,cards):
    while sum(computer) < 17:
        computer.append(deal_cards(cards,1))
    if sum(Computer_cards) > 21:
        display(User_cards,Computer_cards)
        print('Exceeds 21.Dealer Busted.')
    elif sum(User_cards) > sum(Computer_cards):
        display(User_cards,Computer_cards)
        print('You win!! Dealer lost')
    else:
        display(User_cards,Computer_cards)
        print('You lost!! Dealer won')
    return User,computer 
# if we choose n we dont play the game.
def play(Choice):
    if Choice == 'y':
        return True
    else:
        return False
    return restart
Choice = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
restart = play(Choice)
print(logo)
while restart:
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    Continue_game = True
    User_cards = deal_cards(cards,2)
    Computer_cards = deal_cards(cards,2)
    while Continue_game:
        print("Your cards: {}, current score: {}".format(User_cards,sum(User_cards)))
        print(f"Computer's first card: {Computer_cards[0]}")
        Choice = input('Type \'y\' to get another card, type \'n\' to pass: ')
        if Choice == 'y':
            User_cards.append(deal_cards(cards,1))
            if sum(User_cards) > 21:
                display(User_cards,Computer_cards)
                print('You went over.You lose') 
                Continue_game = False     
        else:
            result(User_cards,Computer_cards,cards)
            Continue_game = False
    restart_game = input('Do you want to deal once again? \'y\' or \'n\': ')
    restart = play(restart_game)
