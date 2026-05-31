#Problem 3: Remove First Value
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
    # Check if the list is empty
    if head is None:
        return head

    # If the node to be removed is the head of the list
    if head.value == val:
        return head.next

    # Initialize pointers
    current = head.next
    previous = head

    # Traverse the list to find the node to remove
    while current.next:
        if current.value == val:
            previous.next = current.next
            return head
        previous = current
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