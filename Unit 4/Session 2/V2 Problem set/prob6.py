#Problem 6: Greater Than Threshold
'''Write a function num_of_subarrays() that takes in a list of
 integers nums and two integers k and threshold as parameters. 
 The function returns the number of subarrays of size k whose average
   is greater than or equal to threshold.

def num_of_subarrays(lst, k, threshold):
	pass
Example Usage:

nums = [2,2,2,2,5,5,5,8]
count = num_of_subarrays(lst, 3, 4)
Example Output:

3
# subarrays are [2,5,5], [5,5,5] and [5,5,8]
'''
def num_of_subarrays(lst, k, threshold):
	#calc total sum needed to meet/exceed threshold
    
	thresh = threshold *k
	count = 0
	windowsum = sum(lst[:k]) #sum of the first window of size k

	#check if the first one met condition

	if windowsum >= thresh:
		count +=1
	
	#slide window across

	for i in range(k, len(lst)):
		windowsum += lst[i] - lst[i-k]#update windowsum

		if windowsum >= thresh:
			count +=1

	return count


nums = [2,2,2,2,5,5,5,8]
count = num_of_subarrays(nums, 3, 4)
print(count)