# nested if else
print("Welcome to theme park")
height = int(input("What is your height "))
bill = 0

if height>=90:
    print("you can enter the ride ")
    age = int(input("What is your age "))
    if age<=12:
        bill = 30
        print("please pay 30RS ")
    elif 12> age <=18 :
        bill = 50
        print("please pay 50RS ")    
    else :
        bill = 80
        print("please pay 80RS ")

    photo = input("Do you want a photo taken? Y OR N")
    if photo == 'Y'or'y' :
        bill = bill+10
        print (f"please pay {bill}")    
    else :
        print(f"please pay {bill}")    
else:
    print("You cannot enter the ride ")
print("Thank You for Visiting")    



# character repetion counter
# name3 = name1 + name2
# name4 = name3.lower()
# t = name4.count('t')
# r = name4.count('r')
# u = name4.count('u')
# e = name4.count('e')
# true = t + r + u +  e

# l = name4.count('l')
# o = name4.count('o')
# v = name4.count('v')
# e = name4.count('e')

# love = l + o + v + e

# love_score = str(true) + (love)
# score = int(love_score)
# if score <10 or score>90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif 40< score<50 :
#     print(f"Your score is{score}, you are alright together.")
# else:
#     print(f"your score is{score}")  