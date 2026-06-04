#Problem 11: Length of List
'''Without using the built-in len() function, w
rite a function list_length() that takes in a list lst 
as a parameter and returns the length of the list.

def list_length(lst):
    pass
Example Usage:

lst = [2,4,6,8,10]
length = list_length(lst)
print(length)
Example Output: 5

'''

def list_length(lst):
    all=0
    for i in lst:
        all +=1
    return all

lst = [2,4,6,8,10]
length = list_length(lst)
print(length)