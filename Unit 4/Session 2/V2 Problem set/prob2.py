#Problem 2: Checking Subsequence
'''Write a function is_subsequence that takes in 
two strings s and t as parameters and returns True if s is 
a subsequence of t and False otherwise.

A subsequence of a string is a new string that is formed from 
the original string by deleting some or none of the characters 
without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def is_subsequence(s, t):
	pass
Example Usage:

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))
Example Output:

True
False'''
def is_subsequence(s, t):
	sindex, tindex = 0,0

	while sindex < len(s) and tindex < len(t):
		if s[sindex] == t[tindex]:
			sindex +=1
		tindex +=1
	return sindex == len(s) #if the string is the same length

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))
