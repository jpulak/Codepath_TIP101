#Problem 4: Find Odd Occurrences
'''Write a function find_odd_occurrences() that 
takes in a list of integers numbers where all numbers 
occur an even number of times except for two unique 
numbers that occur an odd number of times. The function 
should find the two unique numbers and return them as a list.
 Assume each problem has exactly one solution.

def find_odd_occurrences(numbers):
    pass
Example Usage:

numbers = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)
Example Output:

[1,3]'''

'''
u
i understand
function, parameters (list of integer) list has even number of frequency
except two, two nums occur odd frequencies, return odds into a list

define function with paramter of list
create new dictionary
putt numbers form list into dictionary(iterate)

initialize new list
iterate through dictionary values to see what is odd
for every odd value, append into new list

edge case, nothing in list, none found(however stated always will be)

'''
def find_odd_occurrences(numbers):
    new={}
    for num in numbers:
        if num not in new:
            new[num] =0
        new[num] +=1

    ans=[]
    for key,val in new.items():
        if val %2!=0:
            ans.append(key)

    return ans 

numbers = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)