import difflib

# List of correct words
correct_words = ["espresso", "cappuccino", "latte"]

#chatGPTed this cz i thought it would be cool
def autocorrect(word, possibilities, n=1, cutoff=0.6):
    """Returns the closest match to the word from the possibilities list."""
    matches = difflib.get_close_matches(word, possibilities, n, cutoff)
    if matches:
        return matches[0]
    return word


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
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def enough_resources(cup):
    for ingredient in MENU[cup]['ingredients']:
        if resources[ingredient] < MENU[cup]['ingredients'][ingredient]:
            print(f"Sorry, there isn't enough {ingredient}.")
            return False
    return True


def process_coins(change=0):
    print("Insert coins:")
    try:
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickels = float(input("How many nickels?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        total = quarters + dimes + nickels + pennies + change
        return total
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return 0


def process_transaction(payment, cost):
    global money
    change = round(payment - cost, 2)
    if payment < cost:
        print("Sorry, that's not enough money. Your amount will be refunded.")
        return False, payment  # Refund the full payment if not enough
    else:
        money += cost  # Add the cost of the drink to the machine's total money
        return True, change


def make_coffee(cup):
    for ingredient in MENU[cup]['ingredients']:
        resources[ingredient] -= MENU[cup]['ingredients'][ingredient]
    print(f"Here is your {cup}. Enjoy!")


def coffee_machine():
    global money
    remaining_change = 0
    should_continue = True
    while should_continue:
        request = input("What would you like? (espresso/latte/cappuccino): ").lower()
        corrected_request = autocorrect(request, correct_words)
        if corrected_request == "off":
            should_continue = False
        elif corrected_request == "report":
            print_report()
        elif corrected_request in MENU:
            print(f"One {corrected_request} costs ${MENU[corrected_request]['cost']}.")
            if enough_resources(corrected_request):
                total_payment = process_coins(remaining_change)
                successful_transaction, change = process_transaction(total_payment, MENU[corrected_request]['cost'])
                if successful_transaction:
                    make_coffee(corrected_request)
                    remaining_change = change
                    while remaining_change > 0:
                        print(f"You have ${remaining_change:.2f} remaining.")
                        another_drink = input("Would you like another drink? (yes/no): ").lower()
                        if another_drink == "no":
                            print(f"Here is your remaining change: ${remaining_change:.2f}")
                            remaining_change = 0
                            break
                        elif another_drink == "yes":
                            request = input("What would you like? (espresso/latte/cappuccino): ").lower()
                            corrected_request = autocorrect(request, correct_words)
                            if corrected_request in MENU:
                                if enough_resources(corrected_request):
                                    successful_transaction, new_change = process_transaction(remaining_change, MENU[corrected_request]['cost'])
                                    if successful_transaction:
                                        make_coffee(corrected_request)
                                        remaining_change = new_change
                                    else:
                                        break
                                else:
                                    break
                            else:
                                print("Invalid selection. Please choose again.")
                        else:
                            print("Invalid selection. Please choose again.")
                else:
                    print("Transaction failed.")
            else:
                print("Sorry, not enough resources to make that drink.")
        else:
            print("Invalid selection. Please choose again.")


coffee_machine()
