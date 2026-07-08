#Problem 12: Printing Linked List
''' Write a function print_linked_list() that 
takes in a head node as a parameter and prints
 the linked list using the string " -> " to separate each node.

Note: The "head" of a linked list is the first
 element in the linked list, equivalent to lst[0] 
 of a normal list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	pass
Example Input:

# input linked list: a->b->c->d->e
print_linked_list(a)
Example Output:

a -> b -> c -> d -> e'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	val = []
	current = head
	while current :
		val.append(current.value)
		current = current.next
	print("->".join(val))


# input linked list: a->b->c->d->e
# --- CREATING THE SAMPLE INPUT ---
# We link each node to the next one manually from right to left
e = Node('e')
d = Node('d', e)
c = Node('c', d)
b = Node('b', c)
a = Node('a', b) # 'a' is now our head node

print_linked_list(a)