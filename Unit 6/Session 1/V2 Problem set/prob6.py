#Problem 6: Was That a Crit?
'''Given the head of a singly linked list, return the number of critical points. A critical point is a local minima or maxima. - The head and tail nodes are not considered critical points. - A node is a local minima if both the next and previous elements are greater than the current element - A node is a local maxima if both the next and previous elements are less than the current element.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def count_critical_points(head):
	pass
Example Usage:

# Input List: 1 -> 2 -> 3 -> 3 -> 3 -> 5 -> 1 -> 3
# Input: head = 3
Example Output:

# Expected Return Value: 2
# Explanation:
#  - Critical point 1 (local maxima) 3 -> 5 -> 1
#  - Critical point 2 (local minima): 5 -> 1 -> 3
'''