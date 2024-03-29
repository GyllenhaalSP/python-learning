"""
Predefined classes for the OOP version of the Coffee Machine Program. By APPBrewery. Modified by GyllenhaalSP.
"""
from menu import MenuItem


class CoffeeMaker:
    """
    Models the machine that makes the coffee
    """
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self) -> None:
        """
        Prints a report of all resources.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        """
        Returns True when the order can be crafted, False if ingredients are insufficient.
        """
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, order: MenuItem) -> None:
        """
        Deducts the required ingredients from the machine resources and gives the user their beverage.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!\n")
