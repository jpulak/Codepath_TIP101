#Problem 5: Transformable Binary Trees by Swapping Subtrees
'''Given the roots of two binary trees root1 and root2, write a function can_transform() that returns True if the tree represented by root1 can be converted to the tree represented by root2 by doing any number of swaps of the first tree’s right and left branches.

Evaluate the time complexity of the function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def can_swap(root1, root2):
	pass

Example Input Tree:

       root1                     root2
         6                         6
        / \                       / \
       /   \                     /   \
      /     \                   /     \
     3       8                 8       3 
    / \     / \               / \     / \
   1   7   4   2             2   4   7   1
          / \   \           /   / \
         7   1   3         3    1  7

Input: root1 = 6, root2 = 6
Expected Output: True
Explanation: 

         6                         6                    6                    6
        / \                       / \                  / \                  / \
       /   \                     /   \                /   \                /   \
      /     \                   /     \              /     \              /     \
     3       8      -->        8       3            8       3            8       3 
    / \     / \               / \     / \          / \     / \          / \     / \
   1   7   4   2             4   2   1   7  -->   2   4   7   1        2   4   7   1
          / \   \           / \   \               \  / \              /   / \
         7   1   3         1   7   3               3 1  7        -->  3   7   1


'''