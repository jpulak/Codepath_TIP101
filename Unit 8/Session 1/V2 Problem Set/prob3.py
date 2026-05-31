#Problem 3: 3-Node Product II
'''Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the product of the values of its two children. Return False otherwise. If the root has only one child, return False.

Evaluate the time complexity of your function.

# Example Input Tree: 
#   10
#  /  
# 10    
# Input: root = 10
# Expected Output: True

# Example Input Tree: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: True

# Example Input Tree: 
#   5
#    \
#     2
# Input: root = 5
# Expected Output: False

# Example Input Tree: Empty Tree (None)
# Input: root = None
# Expected Output: False

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def check_tree(root):
	pass


'''