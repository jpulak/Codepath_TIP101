#Problem 4: Group By Frequency
'''Write a function group_by_frequency() that takes in a list
 lst and returns a dictionary where keys represent the frequency
   of unique elements within lst and values represent a list of 
   elements with the same frequency.

def group_by_frequency(lst):
    pass
Example Usage:

lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))
Example Output:

{ 1 : ['a', 'b'], 2: ['c', 'd'], 3: ['e']}'''


def group_by_frequency(lst):
    new={}
    for i in lst:
        new[i]=new.get(i,0)+1
    
    rev={}
    for letter,num in new.items():
        if num not in rev:
            rev[num]=[]
        rev[num].append(letter)

    return rev


lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))