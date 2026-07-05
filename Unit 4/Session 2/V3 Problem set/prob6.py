#Problem 6: Vowels in Substring
'''Write a function max_vowels() that takes in a string s and an integer k as parameters. The function returns the maximum number of vowel letters in any substring of s with length k. For this question, we consider a, e, i, o, and u as vowels but not y.

def max_vowels(s, k):
	pass
Example Usage:

s = "abciiidef"
print(max_vowels(s, 3))

print(max_vowels(s, 5))
Example Output:

# "iii"
3
# "iiide
4'''

def is_vowel(c):
    # Check if the character is a vowel
    return c in 'aeiou'

def max_vowels(s, k):
    max_vowels, current_vowels = 0, 0
    
    # Initialize the first window and count the vowels in it
    for i in range(k):
        if is_vowel(s[i]):
            current_vowels += 1
    max_vowels = current_vowels
    
    # Slide the window across the string
    for i in range(k, len(s)):
        # If the new character is a vowel, increment current_vowels
        if is_vowel(s[i]):
            current_vowels += 1
        # If the character that's leaving the window is a vowel, decrement current_vowels
        if is_vowel(s[i - k]):
            current_vowels -= 1
        # Update max_vowels if necessary
        max_vowels = max(max_vowels, current_vowels)
        
    return max_vowels

s = "abciiidef"
print(max_vowels(s, 3))

print(max_vowels(s, 5))