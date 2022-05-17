from art import logo

print(logo)

valid_inputs = ['espresso', 'latte', 'cappuccino', 'report', 'off']
user_choice = ''
while user_choice not in valid_inputs:
    user_choice = input("What would you like? espresso/latte/cappuccino").lower()
    if user_choice not in valid_inputs:
        print(f"sorry I don't recognise the option {user_choice}, please have another go")

# start state
resources = {
    'water': 10000,
    'milk': 1000,
    'coffee': 5000,
    'cash': 100}

recipes = {'espresso': {'water': 50, 'milk': 0, 'coffee': 20, 'price': 120},
           'latte': {'water': 50, 'milk': 100, 'coffee': 10, 'price': 100},
           'cappuccino': {'water': 100, 'milk': 50, 'coffee': 10, 'price': 220}}

# handle off

# handle print report
if user_choice == 'report':
    print('Machine report')
    print("water : % s l" % (resources['water'] / 1000))
    print("milk : % s l" % (resources['milk'] / 1000))
    print("coffee : % s g" % (resources['coffee']))
    print("cash : £% s " % (resources['cash']))


# handle transaction

elif user_choice != 'off':
    print(f"You selected {user_choice}")
    active_recipe = recipes[user_choice]

    # handle sufficient resources
    if (active_recipe['water'] > resources['water'] or
            active_recipe['milk'] > resources['milk'] or
            active_recipe['coffee'] > resources['coffee']):
        print('Sorry the machine does not have enough things to make that')
    # Todo need to break this

    # handle coins
    print(f"Cost £{active_recipe['price']/100}")
    deposit = 0
    while deposit < active_recipe['price']:
        coin = input("£1, 50p, 20p, 10p")
        if coin == '£1':
            deposit += 100
        elif coin == '50p':
            deposit += 50
        elif coin == '20p':
            deposit += 20
        elif coin == '10p':
            deposit += 10
        else:
            print('Coin not recognised')
    change = deposit - active_recipe['price']
    print(f"Thank you £{deposit/100} deposited, {user_choice} price £{active_recipe['price']/100}, change £{change/100}")




# handle make coffee
    resources['water'] =- active_recipe['water']
    resources['milk'] =- active_recipe['milk']
    resources['coffee'] =- active_recipe['coffee']
    resources['cash'] += active_recipe['price']

    print("Here's your coffee")