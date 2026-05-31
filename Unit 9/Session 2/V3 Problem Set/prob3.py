#Problem 3: Cousins in Binary Tree
'''Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return True if the nodes corresponding to the values x and y in the tree are cousins, or False otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_cousins(root, x, y):
	pass

Example Input Tree #1:
      1
     / \
    2   3
   / 
  4  
Input: root = 1, x = 4, y = 3
Expected Output: False

Example Input Tree #2:
      1
     / \
    2   3
     \   \
      4   5
Input: root = 1, x = 5, y = 4
Expected Output: True

Example Input Tree #3:
      1
     / \
    2   3
     \   \
      4   5
Input: root = 1, x = 2, y = 3
Expected Output: False


'''