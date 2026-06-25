#Problem 3: Word Follows Pattern
'''Write a function wordPattern() that takes in a 
string pattern and a string s as parameters. 
The function returns True if s follows the pattern
 and False otherwise. The string follows the pattern
   if there is a 1:1 correspondence between a letter 
   in the pattern and a non-empty word in s.

def wordPattern(pattern, s):
    pass
Example Usage:

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))
Example Output:

True
False
False
True
'''

def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    pattern_map = {}
    for index, word in enumerate(words):
        p_char = pattern[index]
        # Did we already use this char for another word?
        if p_char not in pattern_map:
            pattern_map[p_char] = word
        elif pattern_map[p_char] != word:
            return False

    # We couldn't find any mis-matches
    return True