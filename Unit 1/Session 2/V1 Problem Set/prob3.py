#Problem 3: Return Doubled List
'''Modify the function doubled() so that 
instead of printing the items, it returns a new 
list of the doubled numbers.

Example Usage:

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)
Example Output:

[2, 4, 6]'''

def doubled(lst):
    new=[]
    for num in lst:
        new.append(num*2)
    return new

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)