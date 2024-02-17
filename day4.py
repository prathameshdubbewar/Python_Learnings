from collections import namedtuple
import random
# import day2 #can import variables from other modules
# print(day2.a)#can print using '.'
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[0][0])

#Rock ,paper , scissors game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
your_choice =int(input("What are us choosing? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if 0 < your_choice > 3:
    print("Invalid choice, Retry")
else :    
    print("You chose:")
    print(game_images[your_choice])

    system_choice = random.randint(0,2)

    print(f"system chose: {system_choice}")
    print(game_images[system_choice])
    if 0<= your_choice <=2 :
        if system_choice ==2 and your_choice ==0:
            print("You Win")
        elif your_choice ==2 and system_choice == 0:
            print("You Lose")
        elif system_choice > your_choice:
            print("You Lose")
        elif your_choice>system_choice:
            print("You Win")   
        elif your_choice == system_choice :
            print("Its a Draw")     
    else:
        print("invalid input , You Lose")    
