#Problem 4: Skip and Remove Nodes in a Linked List
'''Given the head of a linked list and two integers m and n, traverse the list such that you keep the first m nodes then delete the next n nodes. Continue with this pattern until the end of the list is reached. Return the head of the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


"""
Example usage:

Input: List 1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
Input: head = 1, m = 2, n = 3

Output: 1 -> 2 -> 6 -> 7 
Explanation: Keep first two nodes 1 & 2, delete next three nodes 3, 4, & 5
Keep next two nodes 6 & 7, delete remaining three nodes 8, 9, & 10


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
"""

def skip_and_remove(head, m, n):
	pass


'''