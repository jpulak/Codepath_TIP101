#Problem 9: BST Is Leaf
'''Given a value and the root of a binary search tree, write a function is_leaf_bst() that returns True if a node with the given value is a leaf node and False otherwise. Assume the tree is balanced.

Evaluate the time complexity of your solution.

# Example Input Tree: 
"""
      4
     / \
    /   \
   2     5
  / \    
 1   3    
"""
# Input: root = 4, value = 5
# Expected Output: True

# Example Input Tree: 
"""
      4
     / \
    /   \
   2     5
  / \    
 1   3    
"""
# Input: root = 4, value = 10
# Expected Output: False


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def is_leaf_bst(root, value):
	pass
'''