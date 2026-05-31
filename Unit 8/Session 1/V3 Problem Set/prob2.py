#Problem 2: 3-Node Booleans
'''You are given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child. The left and right child have a boolean value of either True or False.

The root has a string value of either AND or OR. Apply the boolean operation of the root to its two children. Return True if the result of the expression is truth and False otherwise.

Evaluate the time complexity of your function.

# Example Input Tree: 
#    'OR'
#    /   \
#   /     \
# True   False
# Input: root = 'OR'
# Expected Output: True

# Example Input Tree: 
#    'AND'
#    /   \
#   /     \
# True   False
# Input: root = 'AND'
# Expected Output: False

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def tree_expression(root):
	pass


'''