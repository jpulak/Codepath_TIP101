#Problem 3: Path Sum in Binary Tree
'''Given the root of a binary tree and an integer target_sum, return True if the tree has a root-to-leaf path such that adding up all the values along the path equals target_sum. Return False otherwise.

A leaf is a node with no children.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(root, target_sum):
	pass

Example Input Tree #1:

      5
     / \
    4   8
   /   / \  
  11  13  4
 / \       \
7   2       1

Input: root = 5, target_sum = 22
Expected Output: True
Explanation: The root to leaf path 5 -> 4 -> 11 -> 2 sums to 22.

Example Input Tree #2:

    1
   / \
  2   3

Input: root = 1 , target_sum = 5
Expected Output: False
Explanation: There two root-to-leaf paths in the tree:
1 -> 2: The sum is 3.
1 -> 3: The sum is 4.
There is no root-to-leaf path with sum = 5.

'''