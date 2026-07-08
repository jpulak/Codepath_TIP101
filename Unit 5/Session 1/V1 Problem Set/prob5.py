#Problem 5: Choose Pokemon
'''Update the Pokemon class with a new method choose() 
that takes in no parameters except self.

If the Pokemon is caught, the method should print the string 
"<Pokemon name> I choose you!".

Otherwise, it should print "<Pokemon name> is wild! Catch them 
if you can!".

class Pokemon():
	...
	
	def choose(self):
		pass
Example Usage:

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()
Example Output:

{'name': 'rattata', 'types': ['Normal'], 'is_caught': False}
rattata is wild! Catch them if you can!
rattata I choose you!'''

class Pokemon:
	def __init__(self, name, types):
		self.name = name
		self.types = types
		self.is_caught = False
	def print_pokemon(self):
		print( {
			"name": self.name,
			"types": self.types,
			"is_caught": self.is_caught
		})
		
	def catch(self):
		self.is_caught = True
	
	def choose(self):
		if self.is_caught == True:
			print(f"{self.name} I choose you!")
		else:
			print(f"{self.name} is wild! Catch them if you can!")
        

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()