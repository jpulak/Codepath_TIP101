#Problem 6: Interleave Lists
'''Write a function interleave_lists() that accepts two
 lists as parameters. The function should return a new 
 list that combines the given lists by alternating which 
 list it takes its next element from. It will take elements
   in order, and if one list is longer it will append the
     remaining elements to the end of the interleaved list.

def interleave_lists(lst1, lst2):
    pass
Example Usage:

lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst)
Example Output:

[1, 10, 2, 20, 3, 4]
'''

def interleave_lists(lst1, lst2):
    result = []
    
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    length_of_longest_list = max(lst1_len, lst2_len)
	  
    for i in range(length_of_longest_list):
        if i < lst1_len:
            result.append(lst1[i])
        if i < lst2_len:
            result.append(lst2[i])
    return result

lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst)