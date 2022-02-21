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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money_earned = 0


def sufficient_resource(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def calculate_coins():
    print("Please insert coins")
    total_coins = 0
    total_coins += int(input("How many 25 cents? ")) * 0.25
    total_coins += int(input("How many 10 cents? ")) * 0.10
    total_coins += int(input("How many 5 cents? ")) * 0.05
    total_coins += int(input("How many 1 cents? ")) * 0.01
    return total_coins


def sufficient_money(received_money, drink_cost):
    if received_money >= drink_cost:
        change = round(received_money - drink_cost, 2)
        print(f"Here is {change} iin change.")
        global money_earned
        money_earned += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_drink(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients
    print(f"Here is your {drink_name}.")


machine_on = True
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_earned}")
    else:
        selected_drink = MENU[user_input]
        if sufficient_resource(selected_drink["ingredients"]):
            inserted_money = calculate_coins()
            if sufficient_money(inserted_money, selected_drink["cost"]):
                make_drink(selected_drink, selected_drink["ingredient"])



