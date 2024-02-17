# def my_function():
#     for i in range(1,21):
#         if i ==0:
#             print("You got it")

# my_function()



# # REPRODUCE THE BUG 
# from random import randint
# dice_imgs = ["p","q","r","s","t","u"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])


# Play computer

# year = int(input("What is your year of birth\n"))
# if year > 1977 and year <= 2000 :
#     print("You are a genius")
# elif year > 2000 :
#     print("You are a zombie")

# Fix the Errors
# age = int(input("Whats your age\n"))
# if age>18:
#     print(f"You can drive at age of {age} ")

# Print helps in debugging
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages:  "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Use a debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)


# mutate([1,2,3,5,8,13])            

# year = int(input("enter year to check\n "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(" leap year ")
#         else:
#             print("not leap")
#     else :
#         print("leap year")
# else :
#     print("not leap")                    


for number in range(1,100):
    if number % 3 ==0 and number % 5 == 0:
        print("fizbuzz")
    elif number % 3 == 0 :
        print("fizz")
    elif number % 5 == 0 :
        print("buzz")
    else :
        print([number])        
