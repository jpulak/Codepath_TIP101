#Problem 5: BST In-order Predecessor
'''In the remove_bst() problem, we summarized the in-order predecessor of a given node as the largest node in the given node’s left subtree. This is true if the given node has a left subtree.

More generally, the in-order predecessor is the node with the largest key less than the key of the given node. Given the root of a binary search tree, and a TreeNode current, write a function that returns the in-order predecessor of the current node. Assume the tree is balanced.

Evaluate the time complexity of your solution.

class TreeNode():
      def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right
            
def inorder_predecessor(root, current):
      pass
Example Usage:

Example Input Tree #1: (tree depicted using keys)

          10
         /  \
        /    \
       5      15
      / \    
     2   8
    / \
   1   3

Input: root = 10, current = 5
Expected Output: 3

Example Input Tree #2: (tree depicted using keys)

          10
         /  \
        /    \
       5      15
      / \    
     1   8
        / \
       6   9 
 
Input: root = 10, current = 9
Expected Output: 8
'''