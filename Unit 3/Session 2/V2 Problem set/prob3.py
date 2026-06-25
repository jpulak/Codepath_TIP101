#Problem 3: Longest Common Prefix
'''Write a function longest_common_prefix() that
 takes in a list of strings strings as a parameter.
   The function returns the longest common prefix 
   (not substring) of all strings and if there are none,
     it returns an empty string "".

def longest_common_prefix(strings):
    pass
Example Usage:

strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)
Example Output:

fl
'''
'''
find substring of all the strings not just one
so compare for each in list

compare the first of each list, then second then third
'''

def longest_common_prefix(strings):
    if not strings:
        return ""
    

    shortest= strings[0]
    for s in strings:
        if len(s) < len(shortest):
            shortest =s
    for i, char in enumerate(shortest):
        for other in strings:
            if other[i] != char:
                return shortest[::i]
    return shortest

strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)