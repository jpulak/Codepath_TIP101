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
    return my_str[-1::]+my_str[1:-1]+my_str[0]

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

#start:stop:step