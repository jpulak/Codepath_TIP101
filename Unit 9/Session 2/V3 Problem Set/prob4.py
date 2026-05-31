#Problem 4: Print Corner Nodes of Each Level in Binary Tree
'''Given the root of a binary tree, print the value of the corner nodes of every level in a binary tree. The corner nodes are the first and last node in each level of a binary tree.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
def print_corner_nodes(root):
	pass

Example Input Tree 

      6
     / \
    3   8
   /   / \  
  5   4   2
     / \   \
    1   7   3

Expected Output: (Printed)
6
3
8
5 
2
1
3
Explanation:
Level 1: first and last node is 6
Level 2: first node in 3, last node is 8
Level 3: first node is 5, last node is 2
Level 4: first node is 1, last node is 3


'''