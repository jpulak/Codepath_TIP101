#Problem 5: Exclusive Elements
'''Write a function exclusive_elements() that takes in two integer lists lst1 and lst2 as parameters and returns a new list that contains the elements that are exclusively in one list only (elements that are in lst1 but not in lst2 and elements that are in lst2 but not in lst1)

def exclusive_elements(lst1, lst2):
    pass
Example Usage:

lst1 = [3,1,8,10]
lst2 = [4,5,3,7,8]
excl_lst = exclusive_elements(lst1, lst2)
print(excl_lst)
Example Output: [1,10,4,5,7]
'''

def exclusive_elements(lst1, lst2):
    exclusive_lst1 = []
    exclusive_lst2 = []
    
    # Find elements in lst1 that are not in lst2
    for item in lst1:
        if item not in lst2:
            exclusive_lst1.append(item)
    
    # Find elements in lst2 that are not in lst1
    for item in lst2:
        if item not in lst1:
            exclusive_lst2.append(item)
    
    return exclusive_lst1 + exclusive_lst2