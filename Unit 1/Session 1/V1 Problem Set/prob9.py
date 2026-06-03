#Problem 9: First Item
'''Write a function get_first() that takes in a list as a parameter and returns the 
first item in the list. Return None if the list is empty.

def get_first(lst):
    pass
Example Input: [3,1,6,7,5]
Example Output: 3

Note: pass is a keyword that is used as a placeholder for future code'''

def get_first(lst):
    if len(lst) >1:
        return(lst[0])
    else:
        pass

user= input("input list numbers with space: ")

lst =[int(num) for num in user.split()]

print(get_first(lst))
