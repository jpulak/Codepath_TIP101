#Problem 8: Binary Tree Is Leaf  
'''Given a value and the root of a binary search tree, write a function is_leaf_bst() that returns True if a node with the given value is a leaf node and False otherwise. Assume the tree is balanced.

Evaluate the time complexity of your solution.


# Example Input Tree: 
"""
      1
     / \
    /   \
   2     5
  / \    
 4   3    
"""
# Input: root = 1, value = 5
# Expected Output: True

# Example Input Tree: 
"""
      1
     / \
    /   \
   2     5
  /     
 4       
"""
# Input: root = 1, value = 2
# Expected Output: False


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def is_leaf(root, value):
	pass'''