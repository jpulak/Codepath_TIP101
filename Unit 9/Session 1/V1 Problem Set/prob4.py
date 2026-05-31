#Problem 4: Increasing Order Search Tree
'''Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node of the tree is now the root of tree and every node has no left child and only one right child.

Return the root of the modified tree

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasing_bst(root):
	pass

Example Usage:

Example Input Tree #1:

    5
   / \
  1   7


Example Input: root = 5
Expected Output: root = 1

Expected Output Tree #1:

1 
 \
  5
   \
    7


Example Input Tree #2:

       5
      / \
     /   \
    3     6
   / \     \  
  2   4     8
 /         / \
1         7   9

Input: root = 5
Expected Output: root = 1
Expected Output Tree #2:

1
 \
  2
   \
    3
     \
      4
       \
        5 
         \
          6
           \
            7
             \
              8
               \ 
                9


'''