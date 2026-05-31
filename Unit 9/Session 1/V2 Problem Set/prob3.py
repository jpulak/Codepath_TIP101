#Problem 3: Kth Smallest node in a BST
'''Given the root of a binary search tree and a positive integer k, return the value of the kth smallest node in the tree. All nodes in the tree are guaranteed to be unique.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
def kth_smallest(root, k):
	pass

Example Input Tree

          15                     
         /  \                    
        /    \                  
       /      \                 
      10      20               
     /  \     / \            
    8   12   16 26         

Example Input: root = 15, k = 4
Expected Output: 15
Explanation: The 4th smallest value is 15.


'''