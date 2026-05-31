#Problem 4: BST Remove III
'''Use the provided pseudocode to solve the problem below. Given a value and the root of a binary search tree, remove the node with the given value. Return the root of the modified tree.

If multiple nodes with the given value exist, remove the first node you find.

If you need to remove a node with two children, use the deletion by merging strategy. When you delete by merging, you take the two subtrees of the given node and attach the root of the right subtree to the largest node in the left subtree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
		     self.key = key
         self.val = value
         self.left = left
         self.right = right
         
def remove_bst(root, key):
	# Locate the node to be removed
	# If the node is a leaf node:
		# Remove the node by redirecting the appropriate child reference of its parent to None
	# If the node has one parent:
		# Replace the node with its child, updating its parent's nodes child reference appropriately
	# If the node has two children:
		# Find the largest node in the node's left subtree.
		# Set the root of the node's right subtree as the right child of the largest node in the node's left subtree.
	# Return the root of the updated tree
	pass
Example Usage:

Example Input Tree #1: (tree depicted using keys)

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16


Input: root = 10, key = 10
Expected Output: 5
Expected Output Tree:

   5      
  / \     
 1   8
      \
      15
      / \
     13  16       

Explanation: Deleting 10 leaves you with two subtrees. The left subtree has root 5. The right subtree has root 15.
8 is the largest node in the left subtree, so it's right child becomes 15 which is the root of the right subtree.

Example Input Tree #2: (tree depicted using keys)

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16
      \
       9 

Input: root = 10, key = 8
Expected Output: 10 (Should return a node object)
Expected Output Tree

      10
     /  \
    /    \
   5      15
  / \     / \
 1   9  13  16


Example Input Tree #3: (tree depicted using keys)

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16
      \
       9 

Input: root = 10, key = 9
Expected Output: 10 (Should return a node object)
Expected Output Tree

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8  13  16


'''