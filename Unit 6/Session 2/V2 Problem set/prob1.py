#Problem 1: Convert a Singly Linked List to a Circular Linked List 
'''A circular linked list is a linked list where the tail node points at the head node. Write a function that transforms a singly linked list into a circular linked list. Return the head of the linked list. Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def make_circular(head):
	pass
Example Usage:

# Input List: num1 -> num2 -> num3
make_circular(num1)
Result Linked List: num1 -> num2 -> num3 -> num1
'''