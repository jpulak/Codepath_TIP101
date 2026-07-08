#Problem 3: Is Caught
'''Using your code from Problem 2, update your 
squirtle Pokemon so that is_caught is updated to 
True. Use the print_pokemon() function to verify 
that squirtle's is_caught property was updated.

Expected Output:

{
    "name": "Squirtle",
    "types": ["Water"],
    "is_caught": True
}
Example Output

{'name': 'Squirtle', 'types': ['water'], 'is_caught': True}'''

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })

squirtle = Pokemon("Squirtle", ["water"])
squirtle.is_caught = False
squirtle.print_pokemon()