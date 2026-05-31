#Problem 6: Post-order Traversal
'''Given the root of a binary tree, return a list representing the postorder traversal of its nodes' values. In an postorder traversal we traverse the left subtree, then the right subtree, then the current node.

Evaluate the time complexity of your function.

# Example Input Tree: 
"""For example:
      1
     / \
    /   \ 
   2     3
  / \     \ 
 4   5     6
"""
# Input: root = 1
# Expected Output: [4, 5, 2, 6, 3, 1]

# Input: root = None
# Output: []

# Example Input Tree
""" 1 """ 
# Input: root = 1
# Output: [1]

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def postorder_traversal(root):
	pass
'''