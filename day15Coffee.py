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


def isTransactionSuccessful(moneyReceived, drinkCost):
    """Return True when the payment is accepted or return False if the money is insufficient"""
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def makeCoffee(drinkName, orderIngredients):
    """Deduct the required ingredients from the resources"""
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName} ☕️. Enjoy!")
coffeeServed = True

while coffeeServed:
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if coffeeChoice == 'off':
        coffeeServed = False
    elif coffeeChoice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffeeChoice]
        if checkResource(drink['ingredients']):
            payment = processCoins()
            if isTransactionSuccessful(payment, drink["cost"]):
                makeCoffee(coffeeChoice, drink["ingredients"])
