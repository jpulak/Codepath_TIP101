#Problem 6: Add Two Numbers Represented By Linked Lists
'''You are given the heads of two non-empty linked lists l1 and l2 representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
	pass

Example Usage:

Example Input Lists
list1: 2 -> 4 -> 3
list2: 5 -> 6 -> 4

Example Input: l1= 2, l2 = 5
Expected Output: 7
Expected Output List: 7 -> 0 -> 8
Explanation: 342 + 465 = 807

'''