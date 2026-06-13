#Problem 2: Dictionary Intersection
'''Write a function dict_intersection() that takes in two 
dictionaries as parameters and returns a new dictionary 
containing the key-value pairs found in both dictionaries.

def dict_intersection(d1, d2):
    pass
Example Input:

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
Example Output: {'b': 2}'''

def dict_intersection(d1, d2):
    both={}
    for key in d1:
        if key in d2 and d2[key] == d1[key]:
                both[key] = d1[key]

    return both
            


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}

print(dict_intersection(d1, d2))