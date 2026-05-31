#Problem 6: Pre-order Traversal
'''Given the root of a binary tree, return a list representing the preorder traversal of its nodes' values. In a preorder traversal we traverse the current node, then the left subtree, then the right subtree.

# Example Input Tree: 
"""For example:
     1
     / \
    /   \
   2     5
  / \    
 4   3 
"""
# Input: root = 1
# Expected Output: [1, 2, 4, 3, 5]

# Input: root = None
# Output: []

# Example Input Tree
""" 1 """ 
# Input: root = 1
# Output: [1]

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def preorder_traversal(root):
	pass
'''