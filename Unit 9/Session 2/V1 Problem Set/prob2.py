#Problem 2: Find Minimum Depth of Binary Tree
'''Given the root of a binary tree, return its minimum depth. The minimum depth is the number of nodes along the shortest path from the root down to the nearest leaf node.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
        
def min_depth(root):
	pass

Example Usage:

Example Input Tree #1:

   3
  / \
 9  20
    / \  
   15  7

Example Input: root = 3
Expected Output: 2
Shortest path from root node to a leaf node is 3 -> 9. Number of nodes in path is 2.

Example Input Tree #2:

   2
    \
     3
      \
       4
        \
         5
          \
           6        

Example Input: root = 2
Expected Output: 5
Shortest path from root node to a leaf node is 2 -> 3 -> 4 -> 5 -> 6.
Number of nodes in path is 5.

'''