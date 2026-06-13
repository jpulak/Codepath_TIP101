#Problem 3: Filter by Price
'''Write a function that takes in a dictionary of items 
and a price_threshold as parameters. The function should 
iterate through the dictionary and remove all items that
 has a value less than price_threshold. The function also 
 returns a list of all items that are removed. If no item 
 satisfies the condition, return None.

def remove_items_below_price(items, price_threshold):
    pass
Example Usage:

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)
Example Output:

["banana", "date"]
None'''

'''
fucntion, takes in dictionary and a int
iterate through dictionary, remove all items wihtin dictionary 
that is less than given threshold(int)
the removed items(keys) stored into a list an dprinted

define function (items, threshold)
initialize new list
for key, val in items.items():
if val < threshold:
key.append list
items.pop(key)
return list

'''
def remove_items_below_price(items, price_threshold):
    new=[]
    for key,val in list(items.items()):
        if val < price_threshold:
            new.append(key)
            items.pop(key)
    if not new:
        return None
    return new

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)

# def remove_items_below_price(items, price_threshold):
#     # Initialize a list to hold the names of items that will be removed
#     items_to_remove = []

#     # Collect item names to remove in a separate list to avoid modifying the dictionary while iterating
#     for item, price in items.items():
#         if price < price_threshold:
#             items_to_remove.append(item)

#     # Check if any item meets the condition; if not, return None
#     if not items_to_remove:
#         return None

#     # Remove the items from the dictionary and prepare a list of removed items
#     removed_items = []
#     for item in items_to_remove:
#         removed_items.append(item)
#         items.pop(item)

#     return removed_items