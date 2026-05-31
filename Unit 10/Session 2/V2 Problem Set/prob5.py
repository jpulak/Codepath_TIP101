#Problem 5: Insert into a Sorted Circular Linked List
'''Given a linked list node start_node that is a node in a circularly linked list sorted in non-descending order, write a function insert() that inserts a value insert_val into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert(start_node, insert_val):
	pass

Example Usage:

Example Input List
1 ---> 3
^      |
|      | 
4 <-----
Example Input: start_node = 3, insert_val = 2
Expected Output: 3
Expected Output List:
1 ---> 2  --> 3
^             |
|             | 
4 <------------
Explanation: In the figure above, there is a sorted circular list of three elements. 
You are given a reference to the node with value 3, and we need to insert 2 into the list. 
The new node should be inserted between node 1 and node 3. 
After the insertion, the list should look like this, and we should still return node 3.

Example Input List: Empty List
Example Input: start_node = None, insert_val = 1
Expected Output: 1
Explanation: The list is empty (given start_ndoe is None). 
Create a new single circular linked list and return the reference to that single node. 
The node's next value should be itself. 


'''