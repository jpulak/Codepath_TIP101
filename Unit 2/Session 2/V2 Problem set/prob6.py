#Problem 6: How Many Smaller
'''Write a function smaller_numbers_than_current() that takes in a list of numbers nums as a parameter. For each nums[i], the function should find out how many numbers in the list are smaller than it. (For each nums[i], count the number of valid j's such that j!=i and nums[j] < nums[i])

Return the answers in a list.

def smaller_numbers_than_current(nums):
    pass
Example Input:

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))
Example Output: [4,0,1,1,3]

Explanation:

nums[0] == 6
There exists four smaller numbers than it (1, 2, 2 and 3) --> ans[0]=4

nums[1] == 1 
There does not exist any smaller number than it --> ans[1]=0

nums[2] == 2 
There exists one smaller number than it (1) --> ans[2]=1

nums[3] == 2 
There exists one smaller number than it (1) --> ans[3]=1

nums[4] == 3 
There exists three smaller numbers than it (1, 2 and 2) --> ans[4]=3
'''