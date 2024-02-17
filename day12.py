# local Scope
# def drink_coffee():
#     coffee_strength = 1
#     print(coffee_strength)

# drink_coffee()
# print(coffee_strength)

# # Global Scope
# coffee_strength = 10 
# def drink_coffee():
#     coffee_strength = 1
#     print(coffee_strength)

# drink_coffee()
# print(coffee_strength)

# CHOOSE THE NUMBER GAME

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# Defining Function to check users guess


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns-1
    elif guess< answer:
        print("Too Low")
        return turns-1
    else :
        print(f" CORRECT pratik love vinayak, your guess was {answer} ")  

def set_difficulty():
    level = input("Choose dificulty level: Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    

def game():
    print("Welcome to Guessing Game")
    print("Lets choose a number from 1 to 100. ")
    answer = randint(1, 100)

    turns = set_difficulty()
    

    guess = 0
    while guess!=answer:
        print(f"You have {turns} attempts left for the guess ")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns ==0:
            print("Out of moves , YOU LOSE")
            return
        elif guess != answer:
            print("Guess Again")
game()        