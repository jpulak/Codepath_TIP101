#Problem 4: Find Leftmost Path I
'''Given the root of a binary tree, write a function that finds that returns a list of the left most path of the tree.

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
# Expected Output: [1, 2, 4]

# Example Input Tree: 
"""
     1
      \
       2
      / 
     3    
"""
# Input: root = 1
# Expected Output: [1]

# Input: root = None
# Output: []


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def left_path(root):
	pass

'''