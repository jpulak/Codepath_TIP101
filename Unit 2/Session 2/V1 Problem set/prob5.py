#Problem 5: Find Majority Element
'''Write a function find_majority_element() that takes in 
a list of integers elements and finds the majority element 
in the list. A majority element is an element that appears more
 than n/2 times where n is the size of the list. If there is no
   majority element, return None.

def find_majority_element(elements):
    pass
Example Usage:

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
Example Output: 2'''

def find_majority_element(elements):
    new ={}
    for num in elements:
        if num not in new:
            new[num] = 0
        new[num] +=1

    for key,val in new.items():
        if val > len(elements)/2:
            return key
        # else:
        #     return None
    return None

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))