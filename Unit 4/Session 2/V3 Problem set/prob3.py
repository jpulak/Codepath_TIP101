#Problem 3: Backspace Compare
'''Write a function backspace_compare() 
that takes in two strings s and t as 
parameters that both might have the
 backspace character #. The backspace 
 character removes the character in front o
f it. The function returns True if they 
are equal when both are typed into empty 
text editors and False otherwise. Note that
 after backspacing an empty text, the text will continue empty.

def backspace_compare(s, t):
    pass
Example Usage:

s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))

m = "ab##"
n = "c#d#"
print(backspace_compare(m, n))

a = "a#c"
b = "b"
print(backspace_compare(a, b))
Example Output:

True
True
False
'''

def get_next_valid_char_index(string, index):
  # Count of backspaces
  backspace_count = 0
  while index >= 0:
      if string[index] == '#':
          backspace_count += 1
      elif backspace_count > 0:
          backspace_count -= 1
      else:
          break
      index -= 1
  return index


def backspace_compare(s, t):

    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i = get_next_valid_char_index(s, i)
        j = get_next_valid_char_index(t, j)
        
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        if (i >= 0) != (j >= 0):
            # One is at the end, the other isn't
            return False
            
        i -= 1
        j -= 1
    
    return True

s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))

m = "ab##"
n = "c#d#"
print(backspace_compare(m, n))

a = "a#c"
b = "b"
print(backspace_compare(a, b))