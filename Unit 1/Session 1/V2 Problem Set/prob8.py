#Problem 8: Above the Threshold
'''Write a function above_threshold() that takes in a list 
of integers lst and an integer threshold as parameters. 
The function should iterate through the original list and
 return a new list containing only numbers that are greater 
 than threshold.

def above_threshold(lst, threshold):
    pass
Example Usage:

lst = [8,2,13,11,4,10,14]
result = above_threshold(lst, 10)
print(result)
Example Output: [13,11,14]'''

def above_threshold(lst, threshold):
    all =[]
    for num in lst:
        if num >threshold:
            all.append(num)

    return(all)

lst = [8,2,13,11,4,10,14]
result = above_threshold(lst, 10)
print(result)

lst = [1,2,3,4,5,6]
result = above_threshold(lst, 3)
print(result) 