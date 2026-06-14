#Problem 1: Return Book
'''Write a function return_book() that accepts a string title and a 
dictionary library as parameters. library maps book titles to the number 
of copies the library currently has in stock. The function should increment
 the quantity of the book title in library by 1. If title is not in the library,
   then add it and set quantity to 1. Return the updated library dictionary.

def return_book(title, library):
    pass
Example Usage:

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)

Example Output:

{'The Hobbit': 2, '1984': 2, 'The Great Gatsby': 4}
{'The Hobbit': 2, '1984': 1, 'The Great Gatsby': 4, 'The Giver': 1}'''

'''
understand
so i understand tha ti need to writae a function
that takes in two parameters,
a string and a dictionary

the dictionary shows the number of copies of a book, key book, val copies

function should incerement value based on paramter title given 
if tital not in dictionary, add an dset to 1
return the updated dictionary

plan

declare function (title , library)
if title in libaray:
library[title] +=1
else: 
library[title] =1

return library 
implement
'''
def return_book(title, library):
    if title in library:
        library[title] +=1
    else:
        library[title] =1
    return library

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)