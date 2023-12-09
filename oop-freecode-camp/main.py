"""
This .py is create to follow the basics of OOP from freeCodeCamp
link: https://www.youtube.com/watch?v=Ej_02ICOIgs&ab_channel=freeCodeCamp.org
"""
import csv

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


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item_ in items:
            Item(
                name=item_.get('name'),
                price=float(item_.get('price')),
                quantity=int(item_.get('quantity'))
            )


    @staticmethod
    def check_integer(num):
        # We will count out the floats that are point zero
        # for i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

#Item.instantiate_from_csv()
#print(Item.all)
print(Item.check_integer(7))
print(Item.check_integer(7.5))