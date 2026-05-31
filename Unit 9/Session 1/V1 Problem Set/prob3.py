#Problem 3: Minimum Difference in BST
'''Given the root of a binary search tree, return the minimum difference between the values of any two different nodes in the tree.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_diff_in_bst(root):
	pass

Example Usage:

Example Input Tree #1:

    4
   / \
  2   6
 / \  
1   3

Example Input: root = 4
Expected Output: 1 
Explanation: The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)

Example Input Tree  #2: 

   1
  / \
 0  48
    / \  
   12 49

Example Input: root = 1
Expected Output: 1 
Explanation: The smallest difference between any two nodes is 1 (1 - 0 = 1) '''
