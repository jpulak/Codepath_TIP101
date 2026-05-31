#Problem 2: 3-Node Product I
'''Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the product of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.

# Example Input Tree: 
#   10
#  /  \
# 2    5
# Input: root = 10
# Expected Output: True

# Example Input Tree: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def check_tree(root):
	pass

'''