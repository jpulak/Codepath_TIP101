#Problem 2: Dictionary Difference
'''Write a function dict_difference() that takes two 
dictionaries and returns a new dictionary that contains 
only the key-value pairs found only in the first dictionary 
but not in the second.

def dict_difference(d1, d2):
    pass
Example Input:

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d2, d1))
Example Output: {'a': 1, 'c': 3, 'd': 4}'''


'''
understand

i understand that 
i need to make a function that takes in two different dictionaries
return a new dictionary  that only has the key-value pair that is found
ONLY in th efirst dict not in hte second

plan

declare function (d1,d2):
initialize new dictionary
iterate through BOTH key and val in d1
if key and val of d1 not in d2
add that key and val into new dictionary
return new dictionary

implement

'''
def dict_difference(d1, d2):
    new={}
    for key in d1:
        if key not in d2 or d1[key] != d2[key]: 
            new[key] = d1[key]
    return new

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d2, d1))