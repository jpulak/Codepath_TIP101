#Problem 6: Merge Nodes Between Zeros in a Linked List
'''Given the head of a linked list which contains a series of integers separated by 0s, merge the nodes lying between two zero nodes into a single node whose value is the sum of all the merged nodes. The modified list should not contain any zeroes. The head and tail of the list will be nodes with value zero. Return the head of the merged list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

"""
Input List:
0 -> 3- > 1 -> 0 -> 4 -> 5 -> 2 -> 0
Input: head = 0

Expected Return value: 4
Expected Result list: 4 -> 11

Explanation: 3 + 1 = 4, 4 + 5 + 2 = 11

Input List: 
O -> 1 -> 0 -> 3 -> 0 -> 2 -> 2-> 0
Input: head = 0

Expected Return Value: 1
Expected Result List: 1 -> 3 -> 4

Explanation: 1, 3, 2+ 2 = 4

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
"""

def merge_nodes(head):
	pass
'''