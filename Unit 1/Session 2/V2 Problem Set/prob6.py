#Problem 6: Reverse List
'''Write a function reverse_list() that takes in a 
list lst as a parameter and returns a new list containing 
the elements of lst in reverse order.

def reverse_list(lst):
    pass
Example Usage:

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)
Example Output:

[5,4,3,2,1]'''

def reverse_list(lst):
    return lst[::-1]


lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)


# def reverse_list(numbers):
#     reversed_list = []
#     for i in range(len(numbers) - 1, -1, -1):
#         reversed_list.append(numbers[i])
#     return reversed_list

# def reverse_list(numbers):
#     reversed_list = []
#     for number in numbers:
#         reversed_list.insert(0, number)
#     return reversed_list