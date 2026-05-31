#Problem 2: Node Values Between Given Levels in Binary Tree
'''Given the root of a binary tree, return a list of all the node values between to given levels start_level and end_level in a binary tree.

You may assume 1 <= start_level <= end_level <= tree depth.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
def get_level_range(root, start_level, end_level):
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

Example input: root = 3, start_level = 2, end_level = 4
Expected Output: [5, 1, 6, 2, 0, 8, 7, 4]
Explanation:
Level 2 nodes: 5, 1
Level 3 nodes: 6, 2, 0, 8
Level 4 nodes: 7, 4

'''