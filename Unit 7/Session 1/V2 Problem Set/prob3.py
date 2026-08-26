#Problem 3: Recursive Product
'''Write a function list_product() that calculates the product of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?

def list_product(lst):
	pass
Example Usage:
1
# Example Input: [1, 2, 3, 4, 5]
Example Output:sss
 
# Expected Output: 120
# Explanation: 1 * 2 * 3 * 4 * 5 = 120
'''

def list_product(lst):
    if not lst:
        return 1
    else:
        