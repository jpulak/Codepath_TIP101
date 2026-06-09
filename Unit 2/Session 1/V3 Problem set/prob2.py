#Problem 2: Build Inventory
'''Write a function build_inventory() that takes in a 
list of product_names and a corresponding list of 
product_prices as parameters. The function returns a 
dictionary representing the inventory of a small store. 
Each product name in product_names should be a key in the 
dictionary and the corresponding value should be the item 
price.

product_names[i] should be paired with product_prices[i] in the dictionary where 0 <= i <= len(product_names). You may assume that product_names and product_prices are the same length.

def build_inventory(product_names, product_prices):
    pass
Example Input:

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))
Example Output:

{'Apple': 0.99, 'Banana': 0.5, 'Orange': 0.75}'''

def build_inventory(product_names, product_prices):

    invent = {}
    for i in range(len(product_names)):
        names = product_names[i]
        price = product_prices[i]
        invent[names]= price
    return invent
    # invent ={}
    # for i in range (len(product_names)):
    #     invent[product_names[i]]= product_prices[i]
    # return invent

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))