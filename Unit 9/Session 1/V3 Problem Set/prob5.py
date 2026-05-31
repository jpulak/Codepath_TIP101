#Problem 5: Replace Node Value with Sum of Subtree
'''Given a binary tree, in-place replace each nodes value as the sum of all elements present in its left and right subtree. You may assume the value of an empty child node to be 0.

Return the root of the modified tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_transform(root):
	pass

Example Usage:

Example Input Tree

            1
           / \
          /   \ 
         /     \
        2       3
         \     / \
          4    5  6
              / \
             7   8  

Example Input: root = 1
Expected Output: root = 35
Expected Output Tree:

            35
           /  \
          /    \ 
         /      \
        4       26
         \      / \
          0    15  0
              / \
             0   0  
'''