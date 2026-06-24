#Problem 4: Longest Uniform Substring
'''Write a function longest_uniform_substring() that 
takes in a string s and returns the length of the 
longest uniform substring. A uniform substring consists 
of a single repeated character.

def longest_uniform_substring(s):
    pass
Example Usage:

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)
Example Output:

4
1'''

'''
get the highest uniform substring,
the smae character same time
so need to compare the first and the one next to
'''

def longest_uniform_substring(s):
    maxlen = 1
    curr = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr +=1
            maxlen = max(maxlen, curr)
        else:
            curr =1
    return maxlen


s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)