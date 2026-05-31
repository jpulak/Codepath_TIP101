#Problem 1: Merge Sorted Lists
'''The two-pointer approach is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. A common variation of this technique is to point one variable at the beginning of one list/string and a second pointer at the beginning of a second list/string, then increment each pointer conditionally to solve a problem.

Using the two pointer approach, write a function merge_sorted_lists() that takes in two sorted lists lst1 and lst2 as parameters and merges them into a single sorted list. The function returns the new list.

def merge_sorted_lists(lst1, lst2):
    pass
Example Usage:

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged_lst = merge_sorted_lists(lst1, lst2)
print(merged_lst)
Example Output: [1, 2, 3, 4, 5, 6]
'''