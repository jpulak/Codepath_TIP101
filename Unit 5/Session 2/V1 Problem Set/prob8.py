#Problem 8: Linked Listify
'''Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list. The function should return the head of the linked list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_to_linked_list(lst):
    pass
Example Usage:

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)


# This prints ONLY the head node's value:
print(linked_list.value)   # => "Betty"

# (Optional) Traverse to print the whole linked list:
current = linked_list
while current:
    end_arrow = " -> " if current.next else "\n"
    print(current.value, end=end_arrow)
    current = current.next


# Print the head node's VALUE:
print(linked_list.value)        # expected: Betty

Example Output:

Betty

Betty -> Veronica -> Archie -> Jughead

'''