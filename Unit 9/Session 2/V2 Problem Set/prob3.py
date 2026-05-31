#Problem 3: Maximum Nodes at Any Level in Binary Tree
'''Given the root of a binary tree, return the maximum number of nodes in any level of the binary tree.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_max(root):
	pass

Example Usage:

Example Input Tree #1:

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: 2
Explanation: Levels 2 & 3 have 2 nodes each. 

Example Input Tree #2:

       1
      / \
     /   \
    2     3
   / \   / \ 
  4   5 6   7

Example Input: root = 1
Expected Output: 4
Explanation: Level 3 has 4 nodes, the most of any level

'''