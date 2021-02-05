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

def checkResource(orderIngredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in orderIngredients:
        if orderIngredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def processCoins():
    """Returns the total calculated from coins entered"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

coffeeServed = True


while coffeeServed:
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if coffeeChoice == 'off':
        coffeeServed = False
    elif coffeeChoice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: £{profit}")
    else:
        drink = MENU[coffeeChoice]
        if checkResource(drink['ingredients']):
            payment = processCoins()

    # if coffeeChoice == 'espresso':
    #     if resources["water"] < 50:
    #         print("Sorry there is not enough water")
    #     elif resources["coffee"] < 18:
    #         print("Sorry they is not enough coffee")
    # if coffeeChoice == 'latte':
    #     if resources["water"] < 200:
    #         print("Sorry there is not enough water")
    #     elif resources["coffee"] < 24:
    #         print("Sorry they is not enough coffee")
    #     elif resources["milk"] < 150:
    #         print("Sorry there is not enough milk")
    # if coffeeChoice == 'cappuccino':
    #     if resources["water"] < 250:
    #         print("Sorry there is not enough water")
    #     elif resources["coffee"] < 24:
    #         print("Sorry they is not enough coffee")
    #     elif resources["milk"] < 100:
    #         print("Sorry there is not enough milk")
