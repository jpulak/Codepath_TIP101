#Problem 5: Averages of Subarray
'''The sliding window technique is an algorithmic technique 
often used to find a subarray or substring that meets certain 
criteria. It works by initializing two pointers to point at the
 start and end of a ‘window’ or subsection of the string/array at 
 a time. The pointers are then incremented to slide the window and 
 examine a different subarray or substring.

Use the sliding window technique to solve the following problem:

Write a function find_averages_of_subarrays() that takes in a list 
of integers nums and an integer k as parameters. The function returns
 a list where each element in the average of each contiguous subarray
   of size k in nums where 1 ≤k ≤ len(nums)

def find_averages_of_subarrays(k, nums):
	pass
Example Usage:

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)
Example Output:

[2.2, 2.8, 2.4, 3.6, 2.8]
# (1 + 3 + 2 + 6 - 1)/5 = 2.2
# (3 + 2 + 6 -1 + 4)/5 = 2.8
# ... and so forth
'''

def find_averages_of_subarrays(k, nums):
    res = []
    total, start = 0.0, 0
    for end in range(len(nums)):
        total += nums[end] # add next element to window
        if end >= k -1:
            res.append(total/k) #calc average
            total -= nums[start] #remove elemnt going out
            start +=1 #slide window ahead
    return res


# def find_averages_of_subarrays(k, nums):
# 	total = 0
# 	all = []
# 	for i in range(len(nums)-(k-1)):
# 		window = nums[i:i+k]
# 		total = sum(window)/k
# 		all.append(total)
# 	return all

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)
print(avg_lst)