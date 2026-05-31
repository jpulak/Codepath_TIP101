#Problem 1: Is Uni-valued
'''A binary tree is uni-valued if every node in the tree has the same value. Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.

Evaluate the time complexity of your solution.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
	pass
Example Usage:

Example Input Tree #1

      1
     / \
    /   \
   1     1
  / \     \
 1   1     1

Input: root = 1
Expected Output: True

Example Input Tree #2

      1
     / \
    /   \
   1     2
  / \     \
 1   1     1

Input: root = 1
Expected Output: False'''