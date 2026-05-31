#Problem 1: Evaluate Boolean Full Binary Tree
'''You are given the root of a full binary tree with the following properties:

Leaf nodes have either the boolean value True or False .
Non-leaf nodes have either the string value OR or AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return result of evaluating the root node. Return the result of evaluating the root nod

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluate_tree(root):
	pass

Example Input Tree #1:

       OR
      /  \
     /    \
  True    AND
         /   \
       False True  

Input: root = OR
Expected Output: True
Explanation:

       OR                       OR
      /  \                     /  \
     /    \         -->       /    \          -->    True
  True    AND               True   False
         /   \
       False True  
'''