#Problem 5: Get Value
'''Update the Card class with a new method get_value() that takes in no parameters except self.

The function returns the card's value depending on the card's rank:

If the card has rank 2, 3, 4, 5, 6, 7, 8, 9, 10, the method should return the rank as an integer
If the card has rank Ace, the method should return 1 as the card's value
If the card has rank Jack, the method should return 11 as the card's value
If the card has rank Queen, the method should return 12 as the card's value
If the card has rank King, the method should return 13 as the card's value
If the card is invalid, the method should return None
class Card():
	...
	
	def get_value(self):
		pass
Example Usage:

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())
Example Output:

7
11
'''

class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def print_card(self):
		print(f"{self.rank} of {self.suit}")

	def is_valid(self):
		suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
		rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

	def get_value():
		if rank in new

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())