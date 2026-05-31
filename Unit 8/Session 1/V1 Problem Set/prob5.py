#Problem 5: Find Leftmost Node II
'''If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of the function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
	pass

Example Usage:

Example Input Tree #1: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1
Expected Output: 4

Example Input Tree #2: 

     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: 1

Example Input Tree #3:

Input: root = None
Output: None


'''