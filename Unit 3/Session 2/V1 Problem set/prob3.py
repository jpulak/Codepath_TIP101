#Problem 3: Reverse Letters
'''Write a function reverse_only_letters() that 
takes in a string s as a parameter. The function 
reverses the order of the letters in the string and
 returns the new string. Non-letter characters should
   remain in their original positions.

def reverse_only_letters(s):
    pass
Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
Example Output: j-Ih-gfE-dCba

'''

def reverse_only_letters(s):
    all =[]
    for i in s:
        if i.isalpha():
            all.append(i)


    res =""
    end = len(all) -1
    
    for i in s:
        if i.isalpha():
            res += all[end]
            end -= 1
        else:
            res += i
    return res



s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)