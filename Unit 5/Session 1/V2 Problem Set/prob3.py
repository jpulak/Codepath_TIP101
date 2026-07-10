#Problem 3: Verify Update
'''Step 1: Using the same Card class from 
Problem 2, update your code so that the suit of 
card is "Hearts" instead of "Clubs".

Step 2: Use the print_card() method to verify that
 card was updated.

Expected Output: Ace of Hearts'''

class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def print_card(self):
		print(f"{self.rank} of {self.suit}")
card = Card("Clubs","Ace")
card.suit = "Heart"
card.print_card()