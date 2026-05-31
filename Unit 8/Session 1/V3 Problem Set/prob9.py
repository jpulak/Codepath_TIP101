#Problem 9: BST Any Greater
'''Given a value and the root of a binary search tree, write a function contains_greater_bst() which returns True if any nodes greater than value exist in the tree. If no node greater than value exists, return False. Assume the tree is balanced.

Evaluate the time complexity of your solution.

# Example Input Tree: 
"""
      4
     / \
    /   \
   2     5
  / \    
 1   3    
"""
# Input: root = 4, value = 3
# Expected Output:  True

# Example Input Tree: 
"""
      4
     / \
    /   \
   2     5
  / \    
 1   3    
"""
# Input: root = 4, value = 10
# Expected Output: False


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def contains_greater_bst(root, value):
	pass

'''