#Problem 8: Pokemon Evolution
'''Some Pokemon can evolve into other species of Pokemon. 
In the updated Pokemon class below, each instance of Pokemon 
has an attribute evolution. The attribute will either be the
 default value of None or another Pokemon instance.

Write a function get_evolutionary_line() that takes in a 
Pokemon object starter_pokemon as a parameter.

The function should return a list of itself and the Pokemon 
that the starter_pokemon can evolve into.

class Pokemon():
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution
 
def get_evolutionary_line(starter_pokemon):
	pass
Example Usage:

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
Example Output:

[`Charmander`, `Charmeleon`, `Charizard`]
[`Charmeleon`, `Charizard`]
['Charizard']

'''

class Pokemon():
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution
 
def get_evolutionary_line(starter_pokemon):
	line = []
	current = starter_pokemon

	while current:
		line.append(current.name)
		current = current.evolution
	return line

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)