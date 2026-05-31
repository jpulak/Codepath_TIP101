#Problem 3: BST Insert III
'''Given the root of a binary search tree, insert a new node with a given value into the tree. Return the root of the modified tree. If a node with the given value already exists, place the new node in the left subtree. You do not need to maintain a balanced tree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def insert_with_duplicates(root, value):
	pass
Example Usage:

Example Input Tree #1: 

      10
     /  \
    /    \
   8      15
  / \    
 1   6    

Input: root = 10, value = 9 
Expected Output: root = 10
Expected Output Tree:

      10
     /  \
    /    \
   8      15
  / \    
 1   6
      \
       9    


Example Input Tree #2: 

      10
     /  \
    /    \
   8      15
  / \    
 1   6    

Input: root = 10, value = 8
Expected Output: root = 10
Expected Output Tree:

      10
     /  \
    /    \
   8      15
  / \    
 1   6
  \
   8       


Example Input Tree #3: Empty Tree (None)

Input: root = None, value = 4
Expected Output: root = 4
Expected Output Tree:

      4 
'''