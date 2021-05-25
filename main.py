import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_Menu = Menu()

is_on = True

while is_on:
    choice = input(f"What would you like {my_Menu.get_items()} : ").lower()
    if choice == "off":
        print('Shutting Down.....')
        is_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif choice != "latte" and choice != "cappuccino" and choice != "espresso":
        print("You have selected Wrong Choice. Try Again...")
    else:
        drink = my_Menu.find_drink(choice)
        if my_money_machine.make_payment(drink.cost):
            if my_coffee_maker.is_resource_sufficient(drink):
                my_coffee_maker.make_coffee(drink)
