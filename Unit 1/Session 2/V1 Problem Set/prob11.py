#Problem 11: Print the Index
'''Write a function print_indices() that takes in an 
integer list lst as a parameter and prints out the index of
 each item in the given list.
Use the function range() to loop through the list indices.

def print_indices(lst):
    pass
Example Usage:

lst = [5,1,3,8,2]
print_indices(lst)
Example Output:

0
1
2
3
4'''

def print_indices(lst):
    for i in range(len(lst)):
        print(i)

lst = [5,1,3,8,2]
print_indices(lst)