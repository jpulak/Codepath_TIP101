#Problem 5: Equal Tree Split
'''Given the root of a binary tree, return True if removing an edge between two nodes can split the tree into two trees with an equal number of nodes. Return False otherwise.

Evaluate the time complexity of the function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def can_split(root):
	pass

Example Usage:

Example Input Tree #1:

       1
      / \
     /   \
    2     3
   / \     \  
  4   5     7

Example Input: root = 1
Expected Output: True
Explanation: Deleting the edge between node 1 and its left child, node 2 gives the following
two trees, each of size 3

  Tree 1    Tree 2        
              1
               \
    2           3
   / \           \  
  4   5           7



Example Input Tree #2:

       1
      /  \
     /    \
    2      3
   / \    / \  
  4   5  6   7

Example Input: root = 1
Expected Output: False
Explanation: It is not possible to split the tree into two trees of equal size by deleting 
an edge

'''