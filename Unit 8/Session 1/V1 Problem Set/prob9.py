#Problem 9: BST Find
'''Given a value and the root of a binary search tree, write a function find_bst() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def find_bst(root, value):
	pass


# Example Input Tree #1: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4, value = 5
Expected Output: True

Example Input Tree #2: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4, value = 10
Expected Output: False
'''