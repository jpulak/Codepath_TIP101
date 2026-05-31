#Problem 4: Second Minimum Value in a Special Binary Tree
'''Given the root of a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero children. If the node has two children, then this node's value is the smaller value among its two children. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, write a function that returns the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Evaluate the time complexity of the function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def find_second_minimum_value(root):
	pass

Example Input Tree #1:

      2
     / \
    2   5
       / \
      5   7

Example Input: root = 2
Expected Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example Input Tree #2:

      2
     / \
    2   2

Example Input: root = 2
Expected Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value. 
'''