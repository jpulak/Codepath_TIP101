#Problem 5: Add Two Numbers Represented by Linked Lists
'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_two_numbers(head_a, head_b):
    pass

Example Usage:

# list 1: 2 -> 4 -> 3 (342)
# list 2: 5 -> 6 -> 4 (465)
# head_a = 2, head_b = 5

sum = add_two_numbers(head_a, head_b)
print(sum)
Example Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807, so the list is 7 -> 0 -> 8.
'''