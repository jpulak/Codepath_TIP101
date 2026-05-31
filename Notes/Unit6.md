Unit 6 Cheatsheet
Here’s a quick reference sheet for Unit 6. While not an exhaustive list, it highlights the key syntax and concepts you’ll use in this unit, plus a few optional ideas that may help with problem-solving. You’re still expected to know required material from earlier units.
Sections are labeled for clarity:

✅ In-Scope: May appear on the assessment
💡 Not In-Scope: Useful, but not required
🎯 Unit Goals
Solve problems involving singly, doubly, and circularly linked lists
Use the slow and fast pointer method to detect cycles in a linked list
Create a temporary head node to solve problems that require manipulating a linked list's head node
Solve problems requiring multiple traversals of a linked list
Evaluate the time and space complexity of problems involving linked lists
General Concepts ✅ In-Scope
Python Syntax
Chained Assignment
In Python, chained assignment is a convenient shorthand syntax that allows us to assign multiple variables to the same value with a single line of code.

Chained assignment can help improve readability when initializing or updating multiple variables to the same value.

Example Usage:

x = y = z = 3
print(x) # Prints 3
print(y) # Prints 3
print(z) # Prints 3

Break Statements
The break keyword is used to break out of a loop early. When we add a break statement, the loop immediately terminates. Try it

Example Usage:

# Example 1: While Loop
count = 1
while count <= 10:
    if count == 5:
        break  # Break the loop if count reaches 5
    print(count)
    count += 1

# Example 2: For Loop
numbers = [1, 3, 5, 7, 9, 2, 4]
for number in numbers:
    if number % 2 == 0:
        print(f"First even number found: {number}")
        break

Linked Lists
Temporary Head Technique
When we solve linked list problems, we often encounter edge cases that involve the head of a linked list. Common edge cases involving the head of a linked list include:

Deleting the current head of a linked list
Adding a new element to the front of a linked list
Reducing a linked list containing only one node to an empty list
Adding a new node to an empty list
A common technique for handling these edge cases is creating a temporary head node. To apply this technique, an extra node object is created to serve as the temporary head of the list. We can use the temporary head as a placeholder that allows us to easily add items to an empty linked list or manipulate the actual head of a list as if it were any other node.

Example Usage:

The following function accepts the head of a linked list and a value and deletes the first node in the list with the specified value. It returns the head of the modified list.

Example Input List: 1->2->4
Example Input: head = 1, val = 2
Expected Return Value: 1 
Expected Return List: 1->4
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
    
def delete_node(head, val):
    temp_head = Node("temp") # Initialize a temporary head node
    temp_head.next = head    # Point the temporary head at the input list
    
    # Traverse the list
    previous = temp_head
    current = head
    while current:
        if current.value == val:          # If the current node is the node to delete
            previous.next = current.next  # Delete the node
            break                         # Break out of the loop

        previous = current
        current = current.next
    return temp_head.next # Return the head of the input list
Because we created a temporary head, deleting the head of the list can be handled in the same way that deleting any other element in the list is handled. We can also proceed directly to traversing the list without checking if head is None, because the existence of the temporary head means there is at least one node in the list.

[=] Deleting a node without a temporary head
We can still remove a node from a list without the use of a temporary head, but we need to handle edge cases individually.

def delete_node(head, val):
    # Edge case 1: If the list is empty
    if not head:
        return head 
    
    # Edge case 2: If the head node needs to be removed
    if head.value == val:
        return head.next
    
    # Now handle the general case
    previous = None
    current = head
    while current:
        if current.value == val:
            previous.next = current.next
            return head  # Return the head of the list after removal
        previous = current
        current = current.next
    
    return head  # Return the head if no node was removed
[=] ⚠️ Temp Node Terminology
When conducting your own independent research into this technique, you may see the "temp head" technique referred to as the "dummy head" technique. Historically, “dumb” was used as a reference to a member of the deaf community and has negative connotations as a derogatory term. For this reason, CodePath refers to this technique as the "temp head" technique.

Words Matter. We want to call out these terms to increase awareness and ensure that we are inclusive in our communities. If you notice other words or behaviors that are not inclusive, please let a CodePath team member know or email report@codepath.org.

Check out these resources to learn more:

ACM on Words Matter
Lee & Low on the term "Dummy"