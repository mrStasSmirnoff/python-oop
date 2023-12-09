"""
This .py is create to follow the basics of OOP from freeCodeCamp
link: https://www.youtube.com/watch?v=Ej_02ICOIgs&ab_channel=freeCodeCamp.org
"""


class Item:
    pay_rate = 0.8 # class attribute (20% discount)
    def __init__(self, name: str, price: float, quantity):

        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"An instance created: {name}")


    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

#print(item1.calc_total_price())
#print(item2.calc_total_price())
#print(Item.pay_rate) # Accessing class attribute
#print(item1.pay_rate) # class attribute is also available on instance level
#print(item2.pay_rate)

#print(Item.__dict__) # All the attributes for class level
#print(item1.__dict__) # All the attributes for instance level

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)