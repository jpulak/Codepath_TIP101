#Problem 1: Is Even-valued
'''Given the root of a binary tree, return True if every node in the tree has an even value and False otherwise.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_even(root):
	pass
Example Usage:

Example Input Tree #1

      2
     / \
    /   \
   4     10
  / \     \
 6   8     12

Input: root = 2
Expected Output: True

Example Input Tree #2

      2
     / \
    /   \
   4     2
  / \     \
 1   6     8

Input: root = 2
Expected Output: False'''