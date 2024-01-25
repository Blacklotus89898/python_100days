# Coffee machine
MENU = {"latte": 200}
profit = 0



ressources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

while is_on:
    choice = input("Would you likn a coffee?")
    match choice:
        case "off":
            is_on = False
            break
        case "report":
            print(f"Water is: {ressources['water']} ml")
            print(f"Milk is: {ressources['milk']} ml")
            print(f"Coffee is: {ressources['coffee']} ml")
            break # breaks from both loops rip, need to use if else
        case _:
            drink = MENU[choice]
            print(drink)
