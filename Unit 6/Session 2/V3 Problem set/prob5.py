#Problem 5: Rotate a Doubly Linked List to the Left
'''Given the head of a doubly linked list and a non-negative integer k, rotate the list to the left by k places. Return the head of the linked list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


"""
Input List
1 <-> 2 <-> 3 <-> 4 <-> 5
Input: head = 1, k = 2

Expected Return value: 3
Expected Output List: 3 <-> 4 <-> 5 <-> 1 <-> 2

Explanation:
Rotation 1: 2 <-> 3 <-> 4 <-> 5 <-> 1
Rotation 2: 3 <-> 4 <-> 5 <-> 1 <-> 2


Input List
0 <-> 1 <-> 2
Input: head = 0, k = 4

Expected Return value: 1
Expected Output List: 1 <-> 2 <-> 0

Explanation:
Rotation 1: 1 <-> 2 <-> 0
Rotation 2: 2 <-> 0 <-> 1
Rotation 3: 0 <-> 1 <-> 2
Rotation 4: 1 <-> 2 <-> 0
"""

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


def rotate_doubly_linked_list(head, k):
	pass
'''