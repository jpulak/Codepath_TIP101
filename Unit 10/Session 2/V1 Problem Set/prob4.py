#Problem 4: Check Balanced Binary Tree
'''Given the root of a binary tree, return True if the tree is balanced and False otherwise.

A balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def is_balanced(root):
	pass

Example Usage:

Input Tree #1:

      3
     /  \
    9   20
       /  \  
      15   7

Input: root = 3
Output: True

Input Tree #2:

          1
         / \
        2   2
       / \  
      3   3
     / \
    4   4  

Input: root = 1
Output: False


Input Tree #3: Empty Tree
Input: root = 1
Output: True


'''