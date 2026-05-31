#Problem 3: Odd-Even Level Sum Difference in Binary Tree
'''Given the root of a binary tree, return the difference between the sum of all node values in odd levels and sum of all node values in even levels.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_difference(root):
	pass

Example Usage:

Example Input Tree
          6
         / \
        3   8
       /   / \  
      5   4   2
         / \   \
        1   7   3
Expected Output: -5
Explanation: 
Odd level sum: 6 + 5 + 4 + 2 = 17
Even level sum: 3 + 8 + 1 + 7 + 3 = 22
Odd level sum - even level sum: 17 - 22 = -5

'''