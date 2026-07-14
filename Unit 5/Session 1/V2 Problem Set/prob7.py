#Problem 7: Sum of Cards
'''Write a function sum_hand() that takes in an instance of Hand as a parameter and returns the summed value of all cards in the hand.

Use the methods from Problems 5-7 to assist you.
If any card in the hand is invalid, return None.
class Card():
    def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		
	#... methods from previous problems

class Hand:
    def __init__(self):
        self.cards = []
        
	# ... methods from previous problems
		
	
def sum_hand(hand):
	pass
Example Usage:

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)
Example Output: 17'''

class Card():
    def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		
	#... methods from previous problems

class Hand:
    def __init__(self):
        self.cards = []
        
	# ... methods from previous problems
		
	
def sum_hand(hand):
	pass