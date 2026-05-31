#Problem 5: Lowest Common Ancestor in Binary Tree
'''Given the root of a binary tree, find the lowest common ancestor (LCA) of two nodes p and q in the tree. The LCA is the lowest node t that has both p and q as descendant. A node can be considered a descendant of itself.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
def find_lca(root, p, q):
	pass

Example Usage:

Example Input Tree

        3
       / \
      /   \
     /     \
    5       1
   / \     / \  
  6   2   0   8
     / \  
    7   4

Example input: root = 3, p = 5, q = 1
Expected Output: 3
The LCA of nodes 5 and 1 is 3. 

Example Input Tree

        3
       / \
      /   \
     /     \
    5       1
   / \     / \  
  6   2   0   8
     / \  
    7   4

Example input: root = 3, p = 5, q = 4
Expected Output: 5
The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.
'''