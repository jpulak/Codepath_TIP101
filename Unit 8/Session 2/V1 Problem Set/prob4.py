#Problem 4: BST Remove I
'''Use the provided pseudocode to solve the problem below. Given a key and the root of a binary search tree, remove the node with the given key. Return the root of the modified tree.

The tree is sorted by key. If multiple nodes with the given key exist, remove the first node you find. If you need to remove a node with two children, use the in-order successor of that node, which is the smallest value in its right subtree. You do not need to maintain a balanced tree.

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
		# Find the node's inorder successor (smallest node in right subtree)
		# Swap the value of the node and its inorder successor
		# Recursively remove the successor (which now has the current node's value)
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
Expected Output: 13
Expected Output Tree:

      13
     /  \
    /    \
   5      15
  / \       \
 1   8      16


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