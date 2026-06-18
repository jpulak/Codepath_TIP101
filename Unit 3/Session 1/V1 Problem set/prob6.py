#Problem 6: Minimum Distance
'''Write a function min_distance() that takes in a
 list of strings words and two strings word1 and 
 word2' as parameters. The function should return 
 the minimum distance between word1 and word2 in 
 the list of words. The distance between one word
   and an adjacent word in the list is 1.

def min_distance(words, word1, word2):
    pass
Example Usage:

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
Example Output:

3
1
2'''

def min_distance(words, word1, word2):
    pass


words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)