import random
def deal_cards(Cards,n):
    if n == 2:
        cards_drawn = random.choices(Cards,k=n)
    elif n == 1:
        cards_drawn = random.choice(Cards)
    return cards_drawn
def display(User,computer):
        print("Your cards: {}, Final score: {}".format(User,sum(User)))
        print("Computer's Final hand {}, Final score: {}".format(computer,sum(computer)))
        print("You went over.You lose")
Choice = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
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
             Continue_game = False     
    else:    
        Continue_game = False