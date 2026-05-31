#Problem 10: Double to Single
'''Below are the node classes for a singly linked list and a doubly linked list. Write a function dll_to_sll() that takes in the head of a doubly linked list as a parameter and recreates it as a singly linked list.

The function returns the head of the new singly linked list.

class SLLNode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class DLLNode:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def dll_to_sll(dll_head):
	pass
Example Usage:

# DLL: Ice <-> Water <-> Steam
dll_head = Ice
sll_head = dll_to_sll(dll_head)

#SLL: Ice -> Water -> Steam'''