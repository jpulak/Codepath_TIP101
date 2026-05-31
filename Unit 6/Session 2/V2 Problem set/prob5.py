#Problem 5: Circular Linked List Rotate
'''Given the head of a linked list and a non-negative integer k, rotate the list to the right by k places. Return the head of the linked list.

class Node:
    def __init__(self, value, next=None):
        self.value = value

        self.next = next


def rotate_right(head, k):
	pass
Example 1:

# num1 -> num2 -> num3 -> num4 -> num5
new_head = rotate_right(num1, 2)
Expected Output: num4 -> num5 -> num1 -> num2 -> num3

Example 2:

# num1 -> num2 -> num3
new_head = rotate_right(num1, 4)
Expected Output: num3 -> num1 -> num2


'''