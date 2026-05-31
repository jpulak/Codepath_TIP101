#Problem 2: Find Lonely Nodes
'''Given the root of a binary tree, return a list containing the values of all lonely nodes in the tree. Return the list in any order.

A lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def find_lonely_nodes(root):
	pass

Example Input Tree #1:

    1
   / \
  2   3
   \
    4

Input: root = 1
Expected Output: [4]
Explanation: Node 4 is the only lonely node. 
Node 1 is the root and is not lonely
Node 2 and 3 have the same parent and are not lonely


Example Input Tree #2:

     7
    / \
   1   4
  /   / \  
 6   5   3
          \
           2

Input: root = 7
Expected Output: [6,2]  
[2,6] is also an acceptable answer

Example Input Tree #3:

           11
          /  \
         99  88
        /      \  
       77       66
      /          \
     55           44
    /              \
   33               22       

Input: root = 11
Expected Output: [77, 55, 33, 66, 44, 22]  
List elements may be returned in any order
Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
All other nodes are lonely.
'''