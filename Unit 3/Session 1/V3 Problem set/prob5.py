#Problem 5: Longest Substring
'''Write a function that takes in a string s and returns 
the length of the longest substring without repeating 
characters.

def length_of_longest_substring(s):
	pass
Example Usage:

s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)
Example Output:

5
1
'''

'''
takes in a string an dreturn lenght of the longsest substring
that doesnt repeat character

count until the next letter is repeated,

plan
start from the frist letter
variable for first letter
var for coutning
var for final

loop from 1 to the last
compare the var first letter with second letter
if it is different, add count +=1
if it is same, save max(count, final), count =0
'''

def length_of_longest_substring(s):
    start= maxLength =0
    used={}
    for i,char in enumerate(s):
        if char in used and start <= used[char]:
            start= used[char]+1
        else:
            maxLength= max(maxLength, i-start+1)
        used[char]=i
        
    return maxLength
# def length_of_longest_substring(s):
# 	count = 1
# 	final = 0
# 	first = s[0]
# 	for i in range(1,len(s)):
# 		if first != s[i]:
# 			count +=1
# 			first = s[i]
# 		else:
# 			final = max(count, final)
# 			first = s[i]
# 			count = 1
# 	return final 



s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)