#Problem 3: Take from Stock
'''Write a function pop_stock() that takes a dictionary of items items that keeps track of an item and its stock quantity, an item_name, and a quantity to be removed as parameters. The function should remove the specified quantity for that item.
If the item does not exist, return the string "Item does not exist."
If the specified quantity is greater than the stock, return a string "Not enough stock."
If the specified item and quantity do exist within items, decrement the item's stock by the specified quantity and return the updated dictionary.

def pop_stock(items, item_name, quantity):
    pass
Example Usage:

items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

print(resultA)
print(resultB)
print(resultC)
print(resultD)
Example Output:

{'chocolate': 20, 'candy': 3, 'chips': 10}
Not enough stock
Item does not exist
{'chocolate': 15, 'candy': 3, 'chips': 10}'''