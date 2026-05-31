#Problem 9: Convert Singly Linked List to Doubly Linked List
'''One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the code below to convert the singly linked list a doubly linked list.

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold 'Em")
crazy_in_love.next = formation
formation.next = texas_hold_em
Example:

# Current Singly Linked List: Crazy in Love -> Formation -> Texas Hold 'Em
# Desired Doubly Linked List: Crazy in Love <-> Formation <-> Texas Hold 'Em
'''