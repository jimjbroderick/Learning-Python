MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Turn off the Coffee Machine by entering “off” to the prompt
def coffee_machine():
    print('''
            ,-"-. ==========================================
      _r-----i          _          WELCOME  TO  OUR  CAFE!
      {      |-.      ,###.    =============================
       |     | |    ,-------.
       |     | |   c|       |                       ,--.
       |     |'     |       |      _______________ C|  |
       (=====)      =========      !_____________/  `=='   
(HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH)
''')
    take_order()


# Prompt user by asking “What would you like? (espresso/cappuccino/latte):”
def take_order():
    print("Here is our menu:")
    for n in MENU:
        print(f'    {n.capitalize()}')
        print(f'        {MENU[n]}')
    print_report()
    order = input("What would you like? (espresso/cappuccino/latte):\n")
    choice = MENU[order]
    print(f'This will cost {choice["cost"]} '
          f'and will use these ingredients:\n '
          f'    {choice["ingredients"]}')
    check_resources(choice)


# Print report
def print_report():
    print(f'\nHere is how much of the ingredients we currently have:\n'
          f'    {resources["water"]} water left.\n'
          f'    {resources["milk"]} milk left.\n'
          f'    {resources["coffee"]} coffee left.\n')


# Check resources sufficient
def check_resources(choice_for_resources):
    choice_for_ingredients = choice_for_resources["ingredients"]
    order_for_coins = choice_for_resources["cost"]
    if (resources["water"] >= choice_for_ingredients["water"]
            and resources["milk"] >= choice_for_ingredients["milk"]
            and resources["coffee"] >= choice_for_ingredients["coffee"]):
        check_coins(order_for_coins, choice_for_resources)
    else:
        print("Insufficient ingredients.\n")
        print_report()
        return


# Process coins
def check_coins(order_cost, order_for_making):
    print("\nPlease insert coins:")
    given_quarters = int(input("    How many quarters?"))
    given_dimes = int(input("    How many dimes?"))
    given_nickels = int(input("    How many nickels?"))
    given_pennies = int(input("    How many pennies?"))
    total_coins = int(given_quarters) * 25 + int(given_dimes) * 10 + int(given_nickels) * 5 + int(given_pennies) * 1
    customer_change = total_coins - order_cost
    if total_coins >= order_cost:
        print(f'\nHere is your change:\n    {customer_change}')
        make_coffee(order_for_making)
    else:
        print(f'Insufficient funds.😒😒😒\n'
              f'You need {order_cost} to purchase this.\n')
        return


# TODO: Check transaction successful


# TODO: Make coffee
def make_coffee(choice_to_deduct_resources):
    choice_to_deduct_ingredients = choice_to_deduct_resources["ingredients"]
    resources["water"] -= choice_to_deduct_ingredients["water"]
    resources["milk"] -= choice_to_deduct_ingredients["milk"]
    resources["coffee"] -= choice_to_deduct_ingredients["coffee"]
    print('''
           {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  )     Here is your coffee!
   |             | )  )
   |             |/  /     Enjoy!
   |             /  /
   |            (  /
   !             y'
    `-.._____..-'
    ''')
    if input("Would you like to place another order? Y/N").lower() == "y":
        take_order()
    else:
        print("Thank you for your custom! Have a good day!")


coffee_machine()
