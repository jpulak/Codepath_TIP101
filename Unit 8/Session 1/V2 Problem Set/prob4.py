#Problem 4: Find Rightmost Node I
'''Given the root of a binary tree, write a function that finds the value of the right most node in the tree.

Evaluate the time complexity of your function.

# Example Input Tree: 
"""
      1
     / \
    /   \
   2     5
  / \    
 4   3    
"""
# Input: root = 1
# Expected Output: 5

# Example Input Tree: 
"""
     1
      \
       2
      / 
     3    
"""
# Input: root = 1
# Expected Output: 2

# Input: root = None
# Output: None


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_most(root):
	pass'''