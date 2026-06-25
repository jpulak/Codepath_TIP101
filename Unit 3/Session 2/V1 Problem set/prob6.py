#Problem 6: Sum Unique Elements
'''Write a function sum_of_unique_elements() that takes 
in two lists of integers, lst1 and lst2, as parameters
 and returns the sum of the elements that are unique in 
 lst1.

An element is unique if:

it appears exactly once in lst1
it does not appear in lst2
def sum_of_unique_elements(lst1, lst2):
	pass
Example Usage:

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)
Example Output

3
0
'''

'''
take in two lists of intgers
return sum of elements that are unique in lst1
meaning integer appear exactly once in lst 1
and doesnt appear in lst2

so to find this
create a new list to appen dthe unique stuff
for i in lst 1
if i n ot in lst2
i.appen din the new list

.set the whole lsit
sum the list
return the sum
'''

def sum_of_unique_elements(lst1, lst2):
    count = {}
    for num in lst1 + lst2:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    sum_unique = 0
    for num in lst1:
        if count[num] == 1:
            sum_unique += num
    return sum_unique

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)