#Problem 1: List Intersection
'''Using the two_pointer approach, write a function 
find_intersection() that takes in two sorted lists as
 parameters and returns a list containing the intersection
   of the two lists. The intersection list should also be sorted.

The two-pointer approach is a common technique in which we 
initialize two variables (also called a pointer in this context) 
to track different indices or places in a list or string, then
 moves the pointers to point at new indices based on certain 
 conditions. A common variation of this technique is to point 
 one variable at the beginning of one list/string and a second 
 pointer at the beginning of a second list/string, then increment 
 each pointer conditionally to solve a problem.

def find_intersection(lst1, lst2):
    pass
Example Usage:

lst1 = [1,2,4,6,7]
lst2 = [2,3,4,7]
print(find_intersection(lst1, lst2))
Example Output: [2,4,7]'''

def find_intersection(lst1, lst2):
    first, second = 0,0
    new = []

    while first < len(lst1) and second < len(lst2):
        if lst1[first] == lst2[second]:
            new.append(lst1[first])
            first +=1
            second +=1
        elif lst1[first] < lst2[second]:
            first +=1
        else:
            second +=1
    return new
    
lst1 = [1,2,4,6,7]
lst2 = [2,3,4,7]
print(find_intersection(lst1, lst2))