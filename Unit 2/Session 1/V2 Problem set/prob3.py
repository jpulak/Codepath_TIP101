#Problem 3: Dictionary Description

'''The following function get_description() takes in a 
dictionary info and a list keys as parameters. For each key in keys, 
the function prints the value associated with that key in info and prints None if the key does not exist in info.

However, the function has a bug! Copy the function into your IDE 
and run the code. Work with your group members to find the cause of the
 bug and correctly implement the function.

def get_description(info, keys):
    for key in keys:
	    print(info[key])
Example Input:

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)
Expected Output:

Tom
engineer
None
Note: The actual input you see when you run the provided code without fixing the bug may be different!'''