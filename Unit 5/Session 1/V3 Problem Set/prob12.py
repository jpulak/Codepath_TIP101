#Problem 12: Chase String
'''Write a function chase_list() that takes in a head of a linked list and returns a string linking together the values of the list with the separator "chases".

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

Example Usage:

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))
Example Output: "Spike chases Tom chases Jerry chases Gouda"'''