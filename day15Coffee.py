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
coffeeServed = True


while coffeeServed:
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if coffeeChoice == 'off':
        coffeeServed = False
    if coffeeChoice == 'report':
        print(resources)
    if coffeeChoice == 'espresso':
        if resources["water"] < 50:
            print("Sorry there is not enough water")
        elif resources["coffee"] < 18:
            print("Sorry they is not enough coffee")
    if coffeeChoice == 'latte':
        if resources["water"] < 200:
            print("Sorry there is not enough water")
        elif resources["coffee"] < 24:
            print("Sorry they is not enough coffee")
        elif resources["milk"] < 150:
            print("Sorry there is not enough milk")
    if coffeeChoice == 'cappuccino':
        if resources["water"] < 250:
            print("Sorry there is not enough water")
        elif resources["coffee"] < 24:
            print("Sorry they is not enough coffee")
        elif resources["milk"] < 100:
            print("Sorry there is not enough milk")
