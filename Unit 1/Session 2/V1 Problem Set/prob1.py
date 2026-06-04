#Problem 1: Print List
'''Write a function print_list() that takes in a list lst as 
a parameter and prints out each item in the list.

def print_list(lst):
    pass
Example Input:
 lst = ["squirtle", "gengar", "charizard", "pikachu"]
Example Output:

squirtle
gengar
charizard
pikachu'''

def print_list(lst):
    for word in lst:
        print(word)

lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)