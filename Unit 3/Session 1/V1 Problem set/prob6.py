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
    index1, index2 = -1, -1
    min_dist = len(words)  # Use the length of the list as the maximum possible distance
    for i, word in enumerate(words):
        if word == word1:
            index1 = i
            if index2 != -1:#if word 2 alr found
                min_dist = min(min_dist, index1 - index2)
        elif word == word2:
            index2 = i
            if index1 != -1:#if word 1 alr found
                min_dist = min(min_dist, index2 - index1)
    return min_dist if min_dist != len(words) else -1


words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)