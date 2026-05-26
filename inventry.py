inventory = {
    "apples": 50,
    "bananas": 12,
    "oranges": 0,
    "milk": 8,
    "bread": 15
}

item = str(input("Enter an item to check : ")).strip().lower()
if item in inventory:
 quantity = inventory[item]

 if quantity == 0:
    print("Out of Stock")
 else:
   print(f"we have {quantity} in Stock")
else:
  print("Item not available")


 