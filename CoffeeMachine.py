import recipes

class CoffeeMachine:


    def __init__(self, water, milk, coffee, start_cash):
        self.resources =  {}
        self.resources['water'] = water
        self.resources['milk'] = milk
        self.resources['coffee'] = coffee
        self.recipes = recipes
        self.cash = start_cash
        self.current_deposit = 0
        self.message = 'Machine is off'

    def enough_stock(self, selection):
        water_remaining = self.resources['water'] - selection['water']
        milk_remaining = self.resources['milk'] - selection['milk']
        coffee_remaining = self.resources['coffee'] - selection['coffee']

        if (water_remaining<0 or milk_remaining <0  or coffee_remaining <0):
            return False
        else:
            return [water_remaining, milk_remaining, coffee_remaining]

    def add_money(self, money_to_add, recipe):
        self.current_deposit += money_to_add
        message = f"Deposited £{money_to_add}, {recipe['name']} £{recipe['price']} Remaining £{recipe['price']-self.current_deposit} "
        if self.current_deposit < recipe['price']:
            return False
        elif self.current_deposit > recipe['price']:
            return True

    def menu(self):
        menu_readout = ''
        for item in self.recipes:
            if self.enough_stock(item):
                menu_readout+=f"{item['name']}, £{item['price']}\n"
        if menu_readout == '':
            message = "Coffee machine needs servicing, I don't have enough for anything!"
        else:
            message = menu_readout
