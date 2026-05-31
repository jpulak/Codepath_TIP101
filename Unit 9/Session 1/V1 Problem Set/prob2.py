#Problem 2: Root-to-Leaf Paths
'''Given the root of a binary tree, return a list of all root-to-leaf paths in any order.

A leaf is a node with no children.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def binary_tree_paths(root):
	pass

Example Usage:

Example Input Tree #1:

  1
 / \
2   3
 \  
  5         

Example Input: root = 1
Expected Output: ["1->2->5", "1->3"]
["1->3", "1->2->5"] is also valid

Example Input Tree #2:

  1    

Example Input: root = 1
Expected Output: ["1"]

'''