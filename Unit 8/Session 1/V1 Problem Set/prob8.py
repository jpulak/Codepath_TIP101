#Problem 8: Binary Tree Find
'''Given a value and the root of a tree, write a function find() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.

Evaluate the time complexity of your solution.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def find(root, value):
	pass

Example Input Tree #1: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1, value = 5
Expected Output: True

Example Input Tree #2: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1, value = 10
Expected Output: False
'''