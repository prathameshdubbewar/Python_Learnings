##                          *CAESAR CYPHER AND DECYPHER*
##                           ------ ------ --- --------


##   using a single function caesar
##
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cypher_direction):
    end_text = ""
    if cypher_direction == "decode":
            shift_amount *= -1
                
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)###can take iput symbols and numbers and changes only letters 
            new_position = position + shift_amount  #leaving the symbols or numbers untouched
            end_text += alphabet[new_position]
        else:
            end_text += char    
    print(f"The {cypher_direction}d text is {end_text}")


logo = """           
 ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,  
a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8  
8b          ,adPPPPP88  8PP"""""""   `"Y8ba,   ,adPPPPP88  88          
"8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88          
 `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88   
           88               88                                 
           ""               88                                 
                            88                                 
 ,adPPYba, 88  8b,dPPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,  
a8"     "" 88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
8b         88  88       d8  88       88  8PP"""""""  88          
"8a,   ,aa 88  88b,   ,a8"  88       88  "8b,   ,aa  88          
 `"Ybbd8"' 88  88`YbbdP"'   88       88   `"Ybbd8"'  88          
               88                                             
               88           
"""
print(logo)


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text = text, shift_amount = shift, cypher_direction = direction)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")

## Declaring seperate functions
##
# def encrypt(given_text, shift_number):
#     cyphered_text = ""
#     for letter in given_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_number
#         new_letter = alphabet[new_position]
#         cyphered_text += new_letter
#     print(f"The encoded text is : {cyphered_text}")     

# def decrypt(cyphered_text, differing_number):
#     decyphered_text = ""
#     for letter in cyphered_text:
#         position = alphabet.index(letter)
#         new_position = position-differing_number
#         new_letter = alphabet[new_position]
#         decyphered_text = decyphered_text + new_letter
#     print(f"The decoded text is : {decyphered_text}")


# if direction == "encode":
#     encrypt(given_text = text, shift_number = shift) 
# elif direction == "decode":
#     decrypt(cyphered_text = text, differing_number = shift)
# else:
#     print("Invalid input, Try again")           