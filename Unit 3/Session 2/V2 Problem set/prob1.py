#Problem 1: String to Integer
'''Write a function string_to_integer_mapping() that
 takes in a string of digits s as a parameter and returns 
 a list where each element is the integer value of the 
 corresponding digit in the string.

def string_to_integer_mapping(s):
    pass
Example Input: s="12345"
Example Output: [1, 2, 3, 4, 5]
'''

'''
take in a string of digits and then return a list
with each digit in its respective list

i ahve to iterate throught he string and append ot a list
and cast each as a int
'''

def string_to_integer_mapping(s):
    all=[]
    for i in s:
        all.append(int(i))
    return all

s="12345"
print(string_to_integer_mapping(s))