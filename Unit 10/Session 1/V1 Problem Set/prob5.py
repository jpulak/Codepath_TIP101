#Problem 5: Sum Root to Leaf Numbers
'''You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root):
	pass 

Example Usage:

 Example Input Tree #1:

      1
     / \
    2   3

Example Input: root = 1
Expected Output: 25
Explanation: 
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example Input Tree #2:

      4
     / \
    9   0
   / \
  5   1

Input: root = 4
Expected Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root):
    def dfs(node, current_number):
        if node is None:
            return 0
        
        current_number = current_number * 10 + node.val
        
        # If the current node is a leaf, return the current number
        if node.left is None and node.right is None:
            return current_number
        
        # Recursively sum the numbers from the left and right subtrees
        left_sum = dfs(node.left, current_number)
        right_sum = dfs(node.right, current_number)
        
        return left_sum + right_sum
    
    # Start DFS with the root and initial current number as 0
    return dfs(root, 0)

