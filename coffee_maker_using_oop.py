from menu import Menu
from coffee_maker_for_oop import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()

is_on=True
while is_on==True:
  options=menu.get_items()
  choice=input(f"What do you want? ({options}): ")
  if choice=="off":
    is_on=False
  elif choice=="report":
    money_machine.report()
    coffee_maker.report()
  else:
    drink=menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
    else:
      choice1=input("Would you like to refill the resources? 'yes' or 'no'? If yes, You will pay $1.0 for refilling: ")
      if choice1=='yes':
        coffee_maker.refill_resources()
        money_machine.refilling()
      else:
        print("The Machine is Turning off")
        is_on=False
    
    
