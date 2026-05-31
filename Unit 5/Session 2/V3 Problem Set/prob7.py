#Problem 7: Remove Node by Value from Linked List
'''Write a function ll_remove() that takes in the head of a linked list and a value val as parameters.

The function should remove the first node it finds in the linked list with value val and return the head of the linked list. If no node can be found with the value val, return the list unchanged.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_remove(head, val):
    pass 
Example:

# Linked List: 5 -> 6 -> 7 -> 8
# Input: head = 5, val = 6
# Expected Output: 5 -> 7 -> 8'''