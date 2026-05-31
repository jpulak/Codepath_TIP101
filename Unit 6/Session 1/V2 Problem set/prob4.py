#Problem 4: Middle Match
'''A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, and a value val, use the slow-fast pointer technique to determine if val matches the middle node of the list. If there are two middle nodes, return True if the second middle node matches the value val.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def middle_match(head, val):
	pass
Example Usage:

# Input List:
# 1 -> 2 -> 3
# Input: head = 1, val = 2

# Input List:
# 1 -> 2 -> 3 -> 4
# Input: head = 1, val = 2
Example Output:

# Expected Return Value: True
# Expected Return Value: False
'''