#Problem 1: Evaluate Mathematical Expression Tree

'''Evaluate Mathematical Expression Tree You are given the root of a full binary tree with the following properties:

Leaf nodes have an integer value.
Non-leaf nodes have either the string value +, -, *, or /
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. the integer.
Otherwise, evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

Evaluate the time complexity of the function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluate_tree(root):
	pass

Example Usage:

Example Input Tree

        +
      /   \
     /     \
    *       -
   / \     / \
  5   2   60 20 

Input: root = +
Expected Output: 50
Explanation:

        +                         +
      /   \                     /  \
     /     \         -->       10  40          -->    50
    *       -               
   / \     / \
  5   2   60 20 



        '''