#Problem 2: Swap Ends
'''Write a function swap_ends() that accepts a string my_str as
 a parameter and returns a new string where the first and last 
 characters from my_str are swapped.

def swap_ends(my_str):
    pass
Example Usage:

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
Example Output: toab'''

def swap_ends(my_str):
    a=[]
    for i in range(len(my_str)-1,-1,-1):
        a.append(my_str[i])

    return "".join(a)

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)