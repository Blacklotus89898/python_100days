# Coffee machine
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

# db
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

def enough_ingredient(order):
    for item in order:
        if order[item] > resources[item]:
            print(f"Insufficient ingredient: {item}.")
            return False
        else:
            return True
        
def payment():
    print("Please insert coins")
    total = int(input("Quarters: "))*.25
    total += int(input("Dimes:  "))*.1
    total += int(input("Pennies: "))*.01
    return total

def enough_cash(payment, cost):
    return payment > cost

while is_on:
    choice = input("Would you like a coffee?")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water is: {resources['water']} ml")
        print(f"Milk is: {resources['milk']} ml")
        print(f"Coffee is: {resources['coffee']} ml")
        print(f"Profit is: {profit} $")
         # breaks from both loops rip, need to use if else
    else:
        if choice in MENU:
            drink = MENU[choice]
            print(drink)
            if enough_ingredient(drink["ingredients"]):
                if enough_cash(payment(), drink["cost"]):
                    print("success")
            # check if enough ingredients
            # process payment
            # successful -> make coffee
        else:
            print("Invalid input", choice)