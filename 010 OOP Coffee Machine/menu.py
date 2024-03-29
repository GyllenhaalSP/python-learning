"""
Predefined classes for the OOP version of the Coffee Machine Program. By APPBrewery. Modified by GyllenhaalSP.
"""


class MenuItem:
    """
    Models each menu item.
    """
    def __init__(self, name: str, water: int, milk: int, coffee: int, cost: int | float):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """
    Models the coffee machine drink selection menu.
    """
    def __init__(self):
        self.selector = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self) -> str:
        """
        Returns all the names of the available menu items.
        """
        return "".join(f"{item.name}" if item.name == "cappuccino" else f"{item.name}/" for item in self.selector)

    def find_drink(self, order_name: str) -> MenuItem | None:
        """
        Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None.
        """
        for item in self.selector:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
