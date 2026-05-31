#Problem 7: Pop Node
'''Write a function ll_pop() that takes in the head of a linked list and an index i as parameters.

The function should remove the node at index i of the linked list and return the head of the list.

If i is greater than the length of the list, do nothing.
Hint: Linked lists do not have built-in indices so you will need to track the indices yourself.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_pop(head, i):
	pass
Example Usage:

# linked list: num1 -> num2 -> num3
ll_pop(num1, 1)
# result: num1 -> num3'''