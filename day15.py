MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def success_payment(money_received,drink_cost):
    if money_received > drink_cost :
        change_to_return = round(money_received - drink_cost, 2)
        print(f"Here is your {change_to_return} change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. money refunded")
        return False


def resource_sufficiency(ingredients_ordered):
    for item in ingredients_ordered:
        if ingredients_ordered[item] >= resources[item]:
            print(f"Not enough {item}.")
            return False
    return True


def coins_calcu():
    print("Insert coins")
    total = int(input("how many quaters?")) * 0.25
    total += int(input("how many dimes?")) * 0.10
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many penny?")) * 0.01
    return total


def make_coffee(drink_name, ingredients_ordered):
    for item in ingredients_ordered:
        resources[item] -= ingredients_ordered[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else :
        drink = MENU[choice]
        if resource_sufficiency(drink["ingredients"]):
            payment = coins_calcu()
            if success_payment(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



