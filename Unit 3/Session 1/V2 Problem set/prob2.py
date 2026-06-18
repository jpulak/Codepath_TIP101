#Problem 2: Remove Char
'''Write a function remove_char() that takes in a 
string s and an integer n as parameters, The function 
returns a new string with the nth character removed 
where 0 < n < len(s).

def remove_char(s, n):
    pass
Example Usage:

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
Example Output: typo'''

'''
i understand tha tI need to create function,
taking in two parameters
a stringg and a n integer
and the funciton has to find the index of the given integer
wtihin the given string
and remove that character and return the new string

plan
pop the index from the string?
'''

def remove_char(s, n):
    s = [*s]
    del s[n]
    # rem = s.pop(n) rem is the removed item 
    return "".join(s)

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)

# def remove_char(s, n):
#     # Create a new string 'first_part' that includes all characters from the beginning of 's' up to the character at index 'n' (not inclusive).
#     first_part = s[:n]

#     # Create a new string 'last_part' that includes all characters from the character at index 'n+1' to the end of 's'.
#     last_part = s[n+1:]

#     # Return the result by concatenating 'first_part' and 'last_part', effectively removing the character at index 'n'.
#     return first_part + last_part