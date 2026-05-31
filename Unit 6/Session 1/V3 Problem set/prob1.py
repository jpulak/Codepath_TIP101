#Problem 1: The Power of One
'''The following code creates the linked list Ash -> Misty -> Brock. Refactor the code to create the same list with a single line of code.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# Recreate this list in a single line of code
head = Node("Ash")
misty = Node("Misty")
brock = Node("Brock")
head.next = misty
luigi.next = brock'''