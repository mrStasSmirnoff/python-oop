"""
This .py is create to follow the basics of OOP from freeCodeCamp
link: https://www.youtube.com/watch?v=Ej_02ICOIgs&ab_channel=freeCodeCamp.org
"""


class Item:

    pay_rate = 0.8 # class attribute (20% discount)
    all = list()

    def __init__(self, name: str, price: float, quantity):

        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"An instance created: {name}")

        # Actions to execute

        Item.all.append(self)


    def calc_total_price(self):
        return self.price * self.quantity


    def apply_discount(self):
        self.price = self.price * self.pay_rate


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
