import random
def deal_cards(n):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    if n == 2:
        cards_drawn = random.choices(cards,k=n)
    elif n == 1:
        cards_drawn = random.choice(cards)
    return cards_drawn
def calculate(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def display(User,computer):
    print("Your cards: {}, Final score: {}".format(User,sum(User)))
    print("Computer's Final hand {}, Final score: {}".format(computer,sum(computer)))
def compare(userscore,computerscore):
    if userscore == computerscore:
        return "Draw :grimacing:"
    elif computerscore == 0 or computerscore == 21:
        return "Lose, opponent has black jack. :disappointed:"
    elif userscore == 0 or userscore == 21:
        return "Won with a black jack :grinning:"
    elif user_score > 21:
        return "You went over 21.You lost :disappointed:"
    elif computer_score > 21:
        return "You won!! Opponent lost...:smiley:"
    elif userscore > computerscore:
        return "You won!! :grinning:"
    elif userscore < computer_score:
        return "You lost.Opponent won. :disappointed:"
def play(Choice):
    if Choice == 'y':
        return True
    else:
        return False
Choice = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
restart = play(Choice)
while restart:
    Continue_game = True
    User_cards = deal_cards(2)
    Computer_cards = deal_cards(2)
    user_score = calculate(User_cards)
    computer_score =calculate(Computer_cards)
    if user_score == 0 or computer_score == 0:
        display(User_cards,Computer_cards)
        print(compare(user_score,computer_score))
        Continue_game = False
    while Continue_game:
        print("Your cards: {}, current score: {}".format(User_cards,sum(User_cards)))
        print(f"Computer's first card: {Computer_cards[0]}")
        Choice = input('Type \'y\' to get another card, type \'n\' to pass: ')
        if Choice == 'y':
            User_cards.append(deal_cards(1))
            user_score = calculate(User_cards)
            if user_score > 21:
                display(User_cards,Computer_cards)
                print(compare(user_score,computer_score))
                Continue_game = False   
            if user_score == 21:
                print('Most suitable for choice now is \'n\' as user sum is exactly 21.')               
        else:
            while computer_score < 17:
                Computer_cards.append(deal_cards(1))
                computer_score = calculate(Computer_cards)    
            display(User_cards,Computer_cards)
            print(compare(user_score,computer_score))
            Continue_game = False         
    restart_game = input('Do you want to deal once again? \'y\' or \'n\': ')
    restart = play(restart_game)