#Problem 5: Find Mode
'''Write a function find_mode() that takes in a non-empty 
list of integers lst as a parameter. The function returns the 
mode (the most frequently occurring number) and if there is a tie, 
return the element which appeared first in the list.

def find_mode(lst):
    pass
Example Usage:

lst = [1,2,3,2,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)
Example Output: 4

'''

'''
understand

define function(take in list of ints) 
find the most frequent occuring number
if the frequency is the same for multiple, return the num that
came first

edge case- if the frequency is the same
have to look into the list and see what comes first

psudocode

define function (lst)
create frequency map=
create dictionary
iterate through list and implement into dictioary

initialize highest key= 0 or key 1??
iterate through dictioary with key and value(from the second ele?)
if the highest var < value, replace the var with the key


implement

'''

def find_mode(lst):
    new={}
    max_ct =0
    most_frq= None

    for num in lst:
        new[num] = new.get(num, 0) + 1
        # if num not in new:
        #     new[num] = 1
        # else: 
        #     new[num] +=1

        if new[num]> max_ct:
            max_ct = new[num]
            most_frq = num
    return most_frq

lst = [1,2,3,2,3,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)

