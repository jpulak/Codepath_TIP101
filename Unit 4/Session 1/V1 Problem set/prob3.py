#Problem 3: Evaluating Solutions
'''The reverse_list() problem can also be solved
 without using the two pointer technique (as you may 
 have seen it in previous units)! Evaluate the time and 
 space complexity of your two-pointer solution.

Then, evaluate the time and space of the following 
solution:

def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]
Which has better time complexity?
Which has better space complexity?
'''

def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]

'''# time complexity, O(n)
# space complexity(O(n))

#for the copy back using [::1] time is O(n) and space is 
O(n) becuase it creates a new list

for the two pointer, swap in place, time is also O(n)
but space is more efficient O(1) because it only
uses a few variables

 '''