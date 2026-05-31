#Problem 5: Copy Linked List
'''Write a function copy_ll() that takes in the head of a linked_list, and creates a complete copy of that linked list.

The function should return the head of a new linked list which is identical to the given list in terms of its structure and contents, but does not use any of the node objects from the original list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def copy_ll(head):
    pass
Example Usage:

# Linked List: 5 -> 6 -> 7
copy = copy_ll(head) # Linked List Copy: 5 -> 6 -> 7
print(head.value, copy.value)

# Change original list -- should not affect the copy
head.value = 10
print(head.value, copy.value)
Example Output:

5 5
10 5'''