#Problem 5: Reverse Prefix
'''Write a function reverse_prefix() that takes in a 
0-indexed string word and a character ch as parameters. 
The function reverses the segment of word that starts at index 
0 and ends at the index of the first occurrence of ch 
(inclusive) and keeps the rest of the string the same. 
If ch does not exist in word, do nothing. Return the resulting string.

def reverse_prefix(word, ch):
    pass
Example Usage:

word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)
Example Output:

dcbaefd
wollehorld
xyzxyz


iterate through string, fi it matches with the ch
swap wiht the 0 index
'''

def reverse_prefix(word, ch):
    word = [*word]
    if ch in word:
        right = word.index(ch)
    else:
        right = -1

    if right == -1:
        return "".join(word)

    left = 0
    while left< right:
        word[left],word[right] = word[right], word[left]
        left +=1
        right-=1
        
    return "".join(word)

word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)

