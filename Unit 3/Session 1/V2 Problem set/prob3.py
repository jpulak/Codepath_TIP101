#Problem 3: Count Vowels
'''Write a function vowel_count() that takes in a string s
 as a parameter and returns the number of vowels in the given
   string.

def vowel_count(s):
    pass
Example Usage:

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)
Example Output:

3
10
0
'''

def vowel_count(s):
    all=['a','e','i','o','u']
    count =0
    for i in range (len(s)):
        s= s.lower()
        if s[i] in all:
            count +=1
    return count


my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

# def vowel_count(s):
#     vowels = "aeiou"
#     count = 0
#     for char in s:
#         if char.lower() in vowels:
#             count += 1
#     return count