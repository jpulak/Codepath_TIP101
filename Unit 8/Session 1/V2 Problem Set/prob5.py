#Problem 5: Find Rightmost Node II
'''If you implemented the previous right_most() function iteratively, implement it recursively. If you implemented it recursively, implement it recursively.

Evaluate the time complexity of the function.

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