#Problem 4: Consecutive Characters
'''Write a function count_consecutive_characters() 
that takes in a string str1 as a parameter and returns
 the count of the most frequent consecutive character.

def count_consecutive_characters(str1):
    pass
Example Usage:

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)
str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)
Example Output:

4
1

'''



def count_consecutive_characters(str1):

    if not str1:
        return None
    
    most =1
    track = 1
    for i in range(1,len(str1)):
        if str1[i] == str1[i-1]:
            track += 1
        else:
            track = 1
        most = max(most,track)
    return most


  

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)

str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)