#Problem 3: Partition List Around Value
'''Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(head, val):
	pass
Example Input:

# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3
Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3
'''