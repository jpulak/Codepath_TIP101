#Problem 6: Add Pokemon Type
'''Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

It should add new_type to the Pokemon's list of types.

class Pokemon():
	...
	
	def add_type(self, new_type):
		pass
Example Usage:

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
Example Output:

{'name': 'Jigglypuff', 'types': ['Normal'], 'is_caught': False}
{'name': 'Jigglypuff', 'types': ['Normal', 'Fairy'], 'is_caught': False}'''