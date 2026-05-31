#Problem 5: Find the Diameter of Binary Tree
'''Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_diameter(root):
	pass

Example Usage:

Example Input Tree:

     1
    / \
   2   3
  / \  
 4   5

Example Input: root = 1
Output: 3 
3 is the length of the path [4,2,1,3] or [5,2,1,3]
'''