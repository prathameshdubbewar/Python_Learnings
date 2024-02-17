#Functions with Outputs

# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name}{formated_l_name}"

# # formated_string = format_name("PRATHAM","DUBBEWAR")
# print(format_name(input("What is your First name?"),input("What is your Last name?")))

# 
#   CALCAULATOR BUILDING 
# 

# ADD
def add(n1,n2):
    return n1 + n2
# SUBSTRACT
def substract(n1,n2):
    return n1 - n2 
# MULTIPLY
def multiply(n1,n2):
    return n1 * n2
# DIVIDE 
def divide(n1,n2):
    return n1 / n2

operations = {"+":add,"-":substract,"*":multiply,"/":divide}

def calculator():
    should_continue = True
    num1 = float(input("Enter your First number: "))
    for symbol in operations:
        print(symbol)
    while should_continue:
        operation_symbol = input("Pick a operation from above symbols: ")
        num2 = float(input("Enter your Next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculations with {answer}, or type 'n' to start a new calculation ") == 'y':
            num1 = answer
        else:
            should_continue = False    
            calculator()

calculator()


