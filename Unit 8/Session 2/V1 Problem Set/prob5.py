#Problem 5: BST In-order Successor
'''In the remove_bst() problem, we summarized the in-order successor of a given node as the smallest node in the given node’s right subtree. This is true if the given node has a right subtree.

More generally, the in-order successor is the node with the smallest key greater than the key of the given node. Given the root of a binary search tree, and a TreeNode current, write a function that returns the in-order successor of the current node. Assume the tree is balanced.

Evaluate the time complexity of your solution.

class TreeNode():
      def __init__(self, key, value=None, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right
            
def inorder_successor(root, current):
      pass
Example Usage:

# Build Example Tree #1/#2:
#           10
#          /  \
#         5    15
#        / \
#       1   8
#          / \
#         6   9

n1  = TreeNode(1)
n6  = TreeNode(6)
n9  = TreeNode(9)
n8  = TreeNode(8, left=n6, right=n9)
n5  = TreeNode(5, left=n1, right=n8)
n15 = TreeNode(15)
n10 = TreeNode(10, left=n5, right=n15)  # root

# Example 1: current = node with key 5 → successor is node with key 6
succ = inorder_successor(n10, n5)
# Expected: succ is a TreeNode; succ.key == 6

# Example 2: current = node with key 6 → successor is node with key 8
succ = inorder_successor(n10, n6)
# Expected: succ is a TreeNode; succ.key == 8
'''