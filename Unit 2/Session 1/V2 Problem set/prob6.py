#Problem 6: Items to Restock
'''Write a function get_items_to_restock() that takes in a
 dictionary products that maps product names to their
   quantities and an integer restock_threshold as parameters.
     The function returns a list of products that have a value
       less than restock_threshold and need to be restocked. 
       If products is empty, the function return an empty list.


def get_items_to_restock(products, restock_threshold):
    pass
Example Input:

products = {"Product1": 10, "Product2": 2, "Product3": 5, 
"Product4": 3}
restock_threshold = 5
Example Output: ['Product2', 'Product4']'''


def get_items_to_restock(products, restock_threshold):
    if not products:
        return None
    all =[]

    for prod, quant in products.items():
        if quant < restock_threshold:
            all.append(prod)
    return all

    # for stuff in products:
    #     if products[stuff] <restock_threshold:
    #         all.append(stuff)
    # return all

products = {"Product1": 10, "Product2": 2, "Product3": 5, 
"Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold))