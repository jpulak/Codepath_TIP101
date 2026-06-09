#Problem 1: Mountain Peak
'''A mountain list is defined as a list that has
 at least three elements, where there exists some
   i with 0 < i < len(lst)-1 such that lst[0] < 
   lst[1] < ... lst[i-1] < lst[i] and lst[i] > 
   lst[i+1] > ... > lst[len(lst)-1].

Given such a mountain list lst as a parameter,
 write a function that finds and returns the highest 
 peak (the index i of the maximum element).

def peak_index_in_mountain_list(lst):
    pass
Example Usage:

mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)
Example Output: 2'''

def peak_index_in_mountain_list(lst):
    for i in range (1,len(lst)):
        if lst[i] > lst[i+1]:
            return i
   

mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)

'''
1) Loop through the middle elements
 of the list (skip the beginning/end)
2) Compare each element to the next element 
  a) If the next element is bigger, keep looking
  b) If the next element is smaller, return the current 
  index (the peak's position in the list)
'''