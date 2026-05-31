#Problem 2: Sum of Node Values by Level in Binary Tree
'''Given the root of a binary tree, return a list of the sums of node values in each level in the binary tree.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
        
def level_sum(root):
	pass

Example Usage:

Example Input Tree

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: [4, 8, 4]
Explanation: 
Level 1: 4
Level 2: 2 + 6 = 8
Level 3: 1 + 3 = 4
'''