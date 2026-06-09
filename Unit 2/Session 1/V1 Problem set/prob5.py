#Problem 5: Restock Inventory
'''Write a function restock_inventory() that updates an
 inventory dictionary based on a restock list. It accepts 
 two parameters:

current_inventory: a dictionary where each key-value pair 
represents an item and its current stock in the inventory
restock_list: a dictionary where each key-value pair 
represents an item and the quantity to be added to the 
inventory
If an item in restock_list is not present in the
 current_inventory, it should be added. The function 
 should return the updated dictionary current_inventory.

def restock_inventory(current_inventory, restock_list):
    pass
Example Input:

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
Example Output:

{
    "apples": 4 0,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}'''
#provided solution 
# def restock_inventory(current_inventory, restock_list):

#     # Loop over restock_list items to update current_inventory
#     for item, quantity in restock_list.items():
#         if item in current_inventory:
#             current_inventory[item] += quantity
#         else:
#             current_inventory[item] = quantity
    
#     return current_inventory

def restock_inventory(current_inventory, restock_list):
    for k,v in restock_list.items():
        if k in current_inventory:
            current_inventory[k]+=v
        else:
            current_inventory[k] = v
    return current_inventory 


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))