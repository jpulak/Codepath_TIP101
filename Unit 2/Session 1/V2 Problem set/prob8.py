#Problem 8: Quality Control
'''Write a function quality_control() that takes 
in a dictionary product_scores and an integer threshold 
as parameters. The dictionary product_scores has key-value 
pairs that represent a product ID and its quality rating.
If the product has a score greater than or equal
 to threshold, the function categorizes it as a "pass".
If the product has a score less than threshold, the
 function categorizes it as a "fail".
The function returns a new dictionary where the key-value 
pair is the product ID and whether it is a "pass" or "fail".

def quality_control(product_scores, threshold):
    pass
Example Input:

product_scores = {"x0123": 75, "x0124": 40, "x0125": 90,
 "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))
Example Output: {'x0123': 'pass', 'x0124': 'fail', 'x0125': 
'pass', 'x0126': 'fail'}'''

def quality_control(product_scores, threshold):
    for idi,rate in product_scores.items():
        if rate < threshold:
            product_scores[idi]="fail"
        else:
            product_scores[idi]="pass"
    return product_scores

# def quality_control(product_scores, threshold):
#     categorized_products = {}  # Initialize an empty dictionary
#     for product_id in product_scores:
#         if product_scores[product_id] >= threshold:
#             categorized_products[product_id] = "pass"
#         else:
#             categorized_products[product_id] = "fail"
#     return categorized_products

product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))
