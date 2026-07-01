#Problem 5: Reverse Vowels
'''Write a function reverse_vowels() that takes in a string s as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.

def reverse_vowels(s):
    pass
Example Usage:

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)
Example Output:

holle
leotcede
'''
'''
 alist with the vowels
 iterate through the string and take out all
 of teh voewles, and reverse them in a seperate list
 then as you go through the string,
 when it reaches a vowle, repalce with tthe vowel in the
 reversed list
'''
def is_vowel(c):
    return c in 'aeiouAEIOU'

def reverse_vowels(s):
    left =0
    right = len(s)-1
    while left < right:
        


    

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)

# def reverse_vowels(s):
#     all = ['a','e','i','o','u','A','E','I','O','U']
#     save =[]
#     for i in s:
#         if i in all:
#             save.append(i)
#     s = [*s]
#     save = save[::-1]
#     save_point=0
#     for i in range(len(s)):
#         if s[i] in save:
#             s[i] = save[save_point]
#             save_point +=1

#     return "".join(s)