logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

import random
from replit import clear

def deal_cards():
    "RETURNS ANY RANDOM CARD "
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    """ Take a list of cards and return the score calculated from cards """   

    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    #  and return 0 instead of the actual score. 0 will represent a blackjack in our game.
   
    # also this can be USED if 11 in cards and 10 in cards and len(cards) == 2 : 
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    

    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21,
    # remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if sum(cards) > 21 and 11 in cards :
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw. 
# If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0),
#  then the user wins. If the user_score is over 21, then the user loses. 
# If the computer_score is over 21, then the computer loses. If none of the above, 
# then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0 :
        return "Lose, opponent has a BlackJack"
    elif user_score == 0 :
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You Went over. You Lose"
    elif computer_score > 21:
        return "Opponent went over, You WIN"
    elif user_score > computer_score:
        return "You Win"
    else :
        return "You Lose"        

def play_game():
    print(logo)
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    #Hint 11: The score will need to be rechecked with every new card drawn and 
    # the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:


        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or 
        # if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards} and your Current score is: {user_score}")
        print(f" Computers First card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21 :
            is_game_over = True
        else :
                
                #Hint 10: If the game has not ended, ask the user if they want to draw another card. 
                # If yes, then use the deal_card() function to add another card to the user_cards List. 
                # If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another card and Type 'n' to Pass: ")
            if user_should_deal == "y" :
                user_cards.append(deal_cards())
            else:
                is_game_over = True 

    
    #Hint 12: Once the user is done, it's time to let the computer play. 
    # The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    
    print(f"  your final hand: {user_cards}, final score: {user_score}")
    print(f"  computers final hand: {computer_cards}, final score: {computer_score} ")
    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, 
# clear the console and start a new game of blackjack and show the logo from art.py.


while input ("Do you want to play a game of blackjack? type 'y' or 'n': ") == "y" :
    clear()
    play_game()
