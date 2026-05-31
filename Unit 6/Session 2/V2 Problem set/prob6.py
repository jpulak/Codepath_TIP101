#Problem 6: Circular Linked List Delete
'''Given the head of a circularly linked list and a value val, write a function that deletes the first node in the list with value val. Return the head of the modified list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_node(head, val):
	pass
Example 1:

# Example 1:
# Build: 1 -> 2 -> 3 -> (back to 1)
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
head = num1

head = delete_node(head, 2)
# Result Linked List (by values): 1 -> 3 -> 1
Result Linked List: num1 -> num3 -> num1

Example 2:

# Example 2:
# Build: 1 -> 2 -> 3 -> (back to 1)
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
head = num1

head = delete_node(head, 1)   # deleting the head; new head should be 2
# Result Linked List (by values): 2 -> 3 -> 2
Result Linked List: num2 -> num3 -> num2
'''