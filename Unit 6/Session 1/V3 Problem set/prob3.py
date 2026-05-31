#Problem 3: Get it Out of Here!
'''The following code attempts to remove the first node with a given value from a singly linked list based but it contains a bug!

Step 1: Copy this code into your IDE.

Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes a node by value from the list.

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Function with a bug!
def remove_by_value(head, val):
    # Handle empty list and removal from the head
    if not head:
        return None
    if head.value == val:
        return head.next  # Return the second node as the new head

    current = head
    while current.next:
        if current.next.value == val:
            current = current.next.next  # Skip the node with the value
            return head  # Return the original head
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head
Example Usage:

# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 3
Example Output:

# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 4
'''