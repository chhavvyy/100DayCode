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
def is_resource_sufficient(order_ingredients):
       is_enough= True
       for i in order_ingredients:
           if order_ingredients[i] >= resources[i]:
               print(f"sorry there is not enough {i}.")
               is_enough = False
       return is_enough

def process_coins():
    """Return the total calculated from coins inserted."""
    print("PLS INSERT COINS")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received , drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you don't have enough money")
        return False

def make_coffee(drink_name , order_ingredient):
   for i in order_ingredient:
       resources[i] -= order_ingredient[i]
   print(f"here is your {drink_name}")

is_on = True
while is_on:
    choice= input("What would you like? (espresso/latte/cuppucinno)")
    if choice=="off":
        is_on = False
    elif choice=="report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:{resources['profit']}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
             payment = process_coins()
             if is_transaction_successful(payment, drink['cost']):
                 make_coffee(choice, drink['ingredients'])