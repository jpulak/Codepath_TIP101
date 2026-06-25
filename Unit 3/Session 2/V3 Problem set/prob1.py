#Problem 1: Remove Vowels
'''Write a function remove_vowels() that takes in a 
string s as a parameter and returns a new string with 
all the vowels removed. For the purposes of this exercise,
 consider a, e, i, o, and u as vowels and not y. 
 The function should preserve the case of the original 
 letters.

def remove_vowels(s):
    pass
Example Usage:

s = "Hello World"
new_string = remove_vowels(s)
print(new_string)
Example Output: Hll Wrld'''

def remove_vowels(s):
    # Define the vowels to remove
    vowels = "aeiouAEIOU"
    # Initialize an empty string to build the result
    result = ""
    # Iterate through each character in the input string
    for char in s:
        # If the character is not a vowel, add it to the result string
        if char not in vowels:
            result += char
    # Return the result string
    return result

# def remove_vowels(s):
#     vowels = ['a','e','i','o','u']
#     new =""
#     for i in s:
#         if i.lower() not in vowels:
#             new +=i
#     return new

s = "Hello World"
new_string = remove_vowels(s)
print(new_string)