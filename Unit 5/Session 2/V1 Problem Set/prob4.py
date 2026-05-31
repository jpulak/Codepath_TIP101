#Problem 4: Get Tail
'''Write a function get_tail() that takes in the head of a linked list as a parameter.

Return the value of the tail. If the list is empty, return None.

Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
	pass
Example Usage:

# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3

head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3
Example Output: num3
'''