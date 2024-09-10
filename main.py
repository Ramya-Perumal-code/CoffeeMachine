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

loop = True
money = 0.0


def display_report():
    """ display menu item when we type report"""
    for key in resources:
        if key == 'water':
            print(f" Water: {resources[key]}ml")
        if key == 'milk':
            print(f" Milk: {resources[key]}ml")
        if key == 'coffee':
            print(f" Coffee: {resources[key]}g")

    print(f" Money: ${float(money)}")


def check_resources(u_input):
    """ Fn to check resource availability"""
    if resources['water'] < MENU[u_input]['ingredients']['water']:
        return 1
    if resources['coffee'] < MENU[u_input]['ingredients']['coffee']:
        return 2
    if u_input != 'espresso' and resources['milk'] < MENU[u_input]['ingredients']['milk']:
        return 3
    return 0


def calculate_coins(quarter, dime, nickle, pennie):
    """ Fn to calculate price for each menu item"""
    return quarter * 0.25 + dime * 0.10 + nickle * 0.05 + pennie * 0.01


def deduct_resources(u_input):
    """ Fn to deduct the resources from common pool"""
    resources['water'] -= MENU[u_input]['ingredients']["water"]
    resources['coffee'] -= MENU[u_input]['ingredients']["coffee"]
    if u_input != 'espresso':
        resources['milk'] -= MENU[u_input]['ingredients']["milk"]
    return MENU[u_input]["cost"]


while loop:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        loop = False
    if user_input == 'report':
        display_report()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        code = check_resources(user_input)
        if code == 0:
            print("Please insert coins.")
            quarters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickles = float(input("how many nickles?: "))
            pennies = float(input("how many pennies?: "))
            amount = calculate_coins(quarters, dimes, nickles, pennies)
            if amount >= MENU[user_input]['cost']:
                cost = deduct_resources(user_input)
                money += cost
                if amount > cost:
                    print(f"Here is {round(amount - cost, 2)} dollars in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")
        elif code == 1:
            print("Sorry there is not enough water.")
        elif code == 2:
            print("Sorry there is not enough coffee.")
        elif code == 3:
            print("Sorry there is not enough milk.")
