#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.title = title
    self.price = price
    self.quantity = quantity
    self.total = self.total + (price * quantity)
    for _ in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    # total = 80 - (80 * 10 / 100) 
    # total = 80 - 8 = 72
    self.total = self.total - (self.total * self.discount / 100)
    if self.discount:
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def get_items(self):
    return self.items
  
  def void_last_transaction(self):
    self.total = self.total - (self.price * self.quantity)
    for _ in range(self.quantity):
      self.items.pop()
    rounded = round(self.total, 2)
    # print(rounded)
    # print(self.items)
    
# register = CashRegister(10)
# register.add_item("Apple", 1.99, 2)
# register.add_item("Banana", 0.99, 3)
# items = register.get_items()
# print(items)
# register.void_last_transaction()



    

    


   
    
