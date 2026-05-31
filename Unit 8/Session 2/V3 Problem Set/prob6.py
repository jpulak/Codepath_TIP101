#Problem 6: Nested Binary Trees
'''Given the roots of two binary trees root and sub_root, return True if there is a subtree of root with the same structure and node values of sub_root and False otherwise.

A subtree of a binary tree is a tree that consists of a node in and all of this node's descendants. The tree could also be considered as a subtree of itself.

Evaluate the time complexity of your solution.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_subtree(root, sub_root):
	pass
Example Usage:

Example Input Trees #1:

      2                3
     / \              / \
    /   \            6   7  
   3     5
  / \     \
 6   7     12

Input: root = 2, sub_root = 3
Expected Output: True

Example Input Trees #2:

      2                3
     / \              / \
    /   \            1   2  
   3     5
  / \     \
 6   7     12

Input: root = 2, sub_root = 3
Expected Output: False'''