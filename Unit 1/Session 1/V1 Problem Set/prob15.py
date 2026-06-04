#Problem 15: Negative Numbers 
'''Write a function print_negatives() that takes a list of integers lst and 
prints all negative numbers in the list.

def print_negatives(lst):
Example Usage: print_negatives([3,-2,2,1,-5])
Example Output:

-2
-5
Example Usage: print_negatives([1,2,3,4,5])
Example Output:

None'''



import ast
def print_negatives(lst):

    for num in lst:
        if num < 0:
            print(num)

    #my solution
    # all =[]
    # for i in range (len(lst)):
    #     if lst[i]<0:
    #         all.append(lst[i])

    # for i in all:
    #     print(i)

print_negatives([1,-2, 4, 3, -5]) 

print_negatives([1,2,3,4,5]) 

'''  
n= input("list: ")
n= ast.literal_eval(n)

print_negatives(n)
'''

