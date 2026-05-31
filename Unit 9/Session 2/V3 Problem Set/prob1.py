#Problem 1: Level Order Traversal in Dictionary
'''Given the following pseudocode and the root of a binary tree, return a dictionary storing the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).

The dictionarys key should be an integer representing the level. The corresponding value for each key should be a list of node values in that level from left to right.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_dict(root):
    # If the tree is empty:
    # return an empty dictionary

    # Create an empty dictionary
    # Create an empty queue using deque

    # Append a tuple (root, 1) to the queue. The queue will store tuples of (node, level)

    # While the queue is not empty:
    # Pop the next node, level pair off the queue (pop from the left side!)

    # If the level is not yet a key in the dictionary
    # Add to dictionary with empty list as a value

    # Add a tuple with each of the popped node's children
    # and incremented level to the end of the queue
    pass


Example Usage:

Example Input Tree

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: {1: [4], 2: [2, 6], 3: [1, 3]}
Explanation: 
Level 1: Node 4
Level 2 (left to right): Node 2, Node 6
Level 3 (left to right): Node 1, Node 3
'''