#Problem 5: Max Difference
'''Write a function max_difference() that takes 
in a list of integers lst and returns the difference 
between the smallest and largest value in the list.

def max_difference(lst):
    pass
Example Usage:

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
Example Output: 20'''

def max_difference(lst):

    max= lst[0]
    min=lst[0]

    for num in lst:
        if num>max:
            max=num
        if num<min:
            min=num
    return max-min
    # return max(lst)-min(lst)

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)