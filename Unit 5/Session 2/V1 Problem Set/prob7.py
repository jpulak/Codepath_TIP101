#Problem 7: Insert Value
'''Write a function ll_insert() that takes in a head of a linked list, a value val, and an index i as parameters.

The function should insert a new Node with value val at index i of the linked list, then return the head of the linked list.

If i is greater than the length of the list, insert the new node at the end of the list.
Hint: Linked lists do not have built-in indices so you will need to track the indices yourself.

Write a helper function to help you print the new list!

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
	pass
Example Usage:

# linked list: 3 -> 8 -> 12 -> 9
ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9'''