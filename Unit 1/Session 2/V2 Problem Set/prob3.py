#Problem 3: Increment by 1
'''Write a function increment_values() that t
akes in a list of integers lst as a parameter and 
returns a new list containing each element incremented by 1.

def increment_values(lst):
    pass
Example Usage:

lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)
Example Output:

[4, 6, 9, 3]'''

def increment_values(lst):
    new=[]
    for num in lst:
        new.append(num+1)

    return new

lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)

