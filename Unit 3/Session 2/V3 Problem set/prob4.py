#Problem 4: Binary Substrings
'''Write a function binary_substrings_count() that takes in a string s representing a binary number as a parameter. The function counts the number of substrings that satisfy all of the following conditions:

contains an equal number of 0s and 1s
all the 0s in the substring are grouped consecutively
all the 1s in the substrings are grouped consecutively
def binary_substrings_count(s):
    pass
Example Usage:

s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))
Example Output:

# substrings for s: "0011", "01", "1100", "10", "0011", "01"
6
# substrings for s2: "10", "01", "10", "01"
4
# substrings for s3: 
0
'''

def binary_substrings_count(s):
    prev_run_length = 0
    curr_run_length = 1
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr_run_length += 1
        else:
            prev_run_length = curr_run_length
            curr_run_length = 1
        if prev_run_length >= curr_run_length:
            count += 1
    return count