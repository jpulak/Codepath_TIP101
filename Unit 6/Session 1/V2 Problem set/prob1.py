#Problem 1: One to Many
'''The assignment statement to the head variable below creates the linked list Mario -> Luigi -> Wario. Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node("Mario", Node("Luigi", Node("Wario")))
'''