#Problem 4: Flip Signs
'''Write a function flip_sign() that takes in a
 list of integers lst as a parameter and returns a 
 new list where each number in the original list has
   been multiplied by -1.

def flip_sign(lst):
    pass
Example Usage:

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
Example Output:

[-1, 2, 3, -4]
'''

def flip_sign(lst):
    new=[]
    for i in lst:
        new.append(i*-1)
    return new
    
lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
