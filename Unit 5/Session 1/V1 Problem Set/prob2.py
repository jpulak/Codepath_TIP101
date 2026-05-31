#Problem 2: Create Squirtle
'''Step 1: Add the print_pokemon definition below to your code on your IDE.

Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].

Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

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
Example Usage:

squirtle = Pokemon("Squirtle", ["water"])
squirtle.print_pokemon()
Example Output:

{'name': 'Squirtle', 'types': ['water'], 'is_caught': False}'''