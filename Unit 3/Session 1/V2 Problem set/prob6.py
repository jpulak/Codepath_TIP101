#Problem 6: Needle in a Haystack
'''Write a function find_the_needle() that takes in two
 string parameters: a needle and a haystack. The function 
 returns the index of the first occurrence of needle in haystack, 
 or -1 if needle is not part of haystack.

def find_the_needle(haystack, needle):
    pass
Example Usage:

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))
Example Output:

2
-1

'''

def find_the_needle(haystack, needle):

    if not needle:
        return 0
    

    return haystack.find(needle)

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))