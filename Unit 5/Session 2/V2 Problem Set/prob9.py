#Problem 9: Create Double Links
'''One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the Node constructor below so that the code creates a doubly linked list with head <-> tail.

class Node:
	def __init__(self, value, next = None):
	    self.value = value
	    self.next = next

head = Node("First")
tail = Node("Last")

head.next = tail
tail.prev = head
Example Usage:

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)
Example Output:

First <-> Last
First <-> Last'''