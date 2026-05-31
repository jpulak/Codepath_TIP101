#Problem 1: Level Order Traversal of Binary Tree
'''Given the following pseudocode and the root of a binary tree, return a list of the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list

    # Create an empty queue using deque
    # Create an empty list to store the explored nodes

    # Add the root to the queue

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes

    # Add each of the popped node's children to the end of the queue

    # Return the list of visited nodes
    pass


Example Usage:

Example Input Tree:

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: [4, 2, 6, 1, 3]
Explanation: 
Level 1: Node 4
Level 2 (left to right): Node 2, Node 6
Level 3 (left to right): Node 1, Node 3'''