#Problem 10: Last Item
'''Write a function get_last() that takes in a 
list as a parameter and returns the last item in the list. 
Return None if the list is empty.

def get_last(lst):
    pass
Example Input: [3,1,6,7,5]
Example Output: 5'''

def get_last(lst):
    if len(lst)>1:
        return lst[-1]
    else:
        pass


print(get_last([3,1,6,7,5]))


'''user = input("input list w/ space: ")

lst= [int(num) for num in user.split()]

print(get_last(lst))'''