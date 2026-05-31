#Problem 6: Flowerbed
'''Imagine you have a flowerbed in which some of the plots are planted, and some are not. Flowers cannot be planted in adjacent plots.

Write a function can_place_flowers() that takes in an integer list flowerbed containing 0's and 1's, (where 0 is an empty plot and 1 is a planted plot) and an integer n that represents the number of new flowers wanting to be planted as parameters. The function should return True if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and False otherwise.

def can_place_flowers(flowerbed, n):
    pass
Example Usage:

flowerbed = [1,0,0,0,1]
approved = can_place_flowers(flowerbed, 1)
approved2 = can_place_flowers(flowerbed, 2)
print(approved)
print(approved2)
Example Output:

True
False'''