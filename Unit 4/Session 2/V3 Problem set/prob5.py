#Problem 5: Count Negatives
'''The sliding window technique is an algorithmic technique often used to find a subarray or substring that meets certain criteria. It works by initializing two pointers to point at the start and end of a ‘window’ or subsection of the string/array at a time. The pointers are then incremented to slide the window and examine a different subarray or substring.

Use the sliding window technique to solve the following problem:

Write a function count_negatives() that takes in a list of integers lst and a positive number k as parameters. The function returns a list where each element represents the count of the number of negative values of each sublist of size k in lst.

def count_negatives(k, nums):
	pass
Example Usage:

lst = [-1, 2, -2, 3, 5, -7, -5]
print(count_negatives(lst, 3))
Example Output: [2,1,1,1,2]
'''

def count_negatives(lst, k):
    result = []
    start = 0
    count = 0
    
    for i in range(len(lst)):
        if lst[i] < 0:
            count += 1
        
        if (i - start + 1 == k):
            result.append(count)
            if lst[start] < 0:
                count -= 1
                
            start += 1
    
    return result

lst = [-1, 2, -2, 3, 5, -7, -5]
print(count_negatives(lst, 3))