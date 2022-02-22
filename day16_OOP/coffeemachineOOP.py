from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def coffeemachine():
    machine_on = True
    while machine_on:
        user_input = input(f"What would you like? {menu.get_items()}: ")
        if user_input == "off":
            machine_on = False
        elif user_input == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            selected_drink = menu.find_drink(user_input)
            if coffee_maker.is_resource_sufficient(selected_drink) and money_machine.make_payment(selected_drink.cost):
                coffee_maker.make_coffee(selected_drink)





coffeemachine()