#Problem 14: Multiply List
'''Write a function multiply_list() that takes in a
 list of integers lst and an integer multiplier as parameters. 
 The function returns a new list containing each value in lst 
 multiplied by multiplier.

def multiply_list(lst, multiplier):
    pass
Example Usage:

lst = [1,2,3]
new_lst = multiply_list(lst, 3)
Example Output: new_lst = [3,6,9]'''

def multiply_list(lst, multiplier):
    new=[]
    for num in lst:
        new.append(num*multiplier)
    
    return new

lst = [1,2,3]
new_lst = multiply_list(lst, 3)

print(new_lst)