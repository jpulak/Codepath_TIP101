#Problem 4: Two-Pointer Reverse Letters
'''Using the two-pointer approach, write a function reverse_only_letters()
 that takes in a string s as a parameter. The function reverses 
 the order of the letters in the string and returns the new string. 
 Non-letter characters should remain in their original positions.

def reverse_only_letters(s):
    pass
Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
Example Output: j-Ih-gfE-dCba

have two pinter, first in 0 last at end
if they are both lettters, swap the two
if one of them has dash, increase +=1 by that
and then compare those two to swap
'''

def reverse_only_letters(s):
    # Convert the string into a list of characters for easy manipulation
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha:
            right -= 1
        else:
            # Swap the characters
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    # Convert the list of characters back to a string
    return ''.join(chars)

# def reverse_only_letters(s):
#     first = 0
#     last = len(s) -1
#     s = [*s]
#     while first < last:
#         if s[first].isalpha() and s[last].isalpha():
#             s[first],s[last]= s[last],s[first]
#             first +=1
#             last -=1
#         elif not s[first].isalpha():
#             first +=1
#         else:
#             last -=1
#     return "".join(s)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)