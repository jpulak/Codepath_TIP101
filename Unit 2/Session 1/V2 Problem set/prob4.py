#Problem 4: Sum Even Values
'''Write a function sum_even_values() that returns
 the sum of all even values in a given dictionary.
   Assume the dictionary values are all integers.

def sum_even_values(dictionary):
    pass
Example Usage:

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))
Example Output: 14'''

def sum_even_values(dictionary):
    total =0
    for i in dictionary.values():
        if i%2 ==0:
            total += i
    return total

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))

#bracket notation
# def sum_even_values(dictionary):
#     sum_even = 0
#     for key in dictionary:
#         if dictionary[key] % 2 == 0:
#             sum_even += dictionary[key]
#     return sum_even

