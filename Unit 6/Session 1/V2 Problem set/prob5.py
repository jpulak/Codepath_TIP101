#Problem 5: Where Do We Begin?
'''A linked list contains a cycle if the tail element points back to another element in the list. Given the head of a linked list, use the fast and slow pointer method to determine the node where the cycle starts. If the linked list does not contain a cycle, return None.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def get_loop_start(head):
	pass
Example Usage:

# Input List:
# 1 -> 2 -> 3 -> 4
#      ^         | 
#      |---------|
# Input: head = 1
Example Output:

# Output: 2
'''