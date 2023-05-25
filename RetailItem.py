#Brian Webb
#ITEC209
#RetailItem Class
#4/15/2023

class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

    def __str__(self):
        return f'{self.description} ({self.units_in_inventory} in stock) - ${self.price:.2f}'

item1 = RetailItem('Jacket', 12, 59.95)
item2 = RetailItem('Designer Jeans', 40, 34.95)
item3 = RetailItem('Shirts', 20, 24.95)

print(item1)
print(item2)
print(item3)
