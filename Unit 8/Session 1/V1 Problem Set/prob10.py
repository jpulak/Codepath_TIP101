#Problem 10: BST Descending Leaves
'''Given the root of a binary search tree, write a function descending_leaves() that returns a list of the values of all leaves in the BST in descending order. Assume the tree is balanced.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def descending_leaves(root):
	pass

Example Input Tree #1: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: [5, 3, 1]

Example Input Tree #2: 
 10 

Input: root = 4
Expected Output: [10]

'''