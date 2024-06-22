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
money = 0
def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml  "
          f"\nCoffee: {resources['coffee']}g\nMoney: ${money:.2f}")

def enough_resources(cup):
    for ingredient in MENU[cup]['ingredients']:
        if resources[ingredient] < MENU[cup]['ingredients'][ingredient]:
            print(f"Sorry, there isn't enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Insert coins:")
    try:
        quarters = float(input("How many quarters? (A quarter is $0.25): ")) * 0.25
        dimes = float(input("How many dimes? (A dime is $0.1): ")) * 0.10
        nickels = float(input("How many nickels? (A nickel is $0.05): ")) * 0.05
        pennies = float(input("How many pennies? (A penny is $0.01): ")) * 0.01
        total = quarters + nickels + dimes + pennies
        return total
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return 0


def process_transaction(payment, cost):
    global money
    if payment < cost:
        print("Sorry, that's not enough money. Your amount will be refunded.")
        return False
    elif payment >= cost:
        change = round(payment - cost, 2)
        if change != 0:
            print(f"Here is ${change:.2f} in change.")
        money += cost
        return True

def make_coffee(cup):
    for ingredient in MENU[cup]['ingredients']:
        resources[ingredient] -= MENU[cup]['ingredients'][ingredient]
    print(f"Here is your {cup}. Enjoy!")


should_continue = True
while should_continue:
    request = input("What would you like? (espresso/latte/cappuccino):").strip().lower()
    if request == "off":
        should_continue = False
    elif request == "report":
        print_report()
    elif request in MENU:
        print(f"One {request} costs ${MENU[request]['cost']}.")
        if enough_resources(request):
            pay = process_coins()
            if process_transaction(pay, MENU[request]['cost']):
                make_coffee(request)
    else:
        print("This item is not on the menu. Please choose again.")
