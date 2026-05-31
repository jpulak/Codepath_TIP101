#Problem 7: Binary Tree All Lesser
'''Given the root of a binary tree and a value val, write a function is_lesser() that returns True if all the nodes in the tree have a value less than val and False otherwise. If the tree is empty, return False.

Evaluate the time complexity of your function.

# Example Input Tree: 
"""
      4
     / \
    /   \
   2     5
  / \    
 1   3    
"""
# Input: root = 4, val = 5
# Expected Output: False

# Example Input Tree: 
"""
      4
     / \
    /   \
   2     5
  / \    
 1   3    
"""
# Input: root = 4, val = 6
# Expected Output: True


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def is_lesser(root, val):
	pass
'''