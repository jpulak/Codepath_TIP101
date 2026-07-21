#Problem 6: Hand Class
'''Step 1: Add the following Hand class to your code that represents a player's hand of cards.

A new instance of Hand is always empty.
class Hand:
    def __init__(self):
        self.cards = []
     
    def add_card(self, card):
	    pass
	    
	def remove_card(self, card):
		pass
Step 2: Add two methods add_card() and remove_card() to the Hand class that each accept a Card object as a parameter.

add_card() should add the Card to the player's Hand
remove_card() should remove the card from the player's Hand.sdf
Example Usage:

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)dfgdf
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]
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

    def get_value(self):
        if self.rank == "Ace":
            return 1
        elif self.rank == "Jack":
            return 11
        elif self.rank == "Queen":
            return 12
        elif self.rank == "King":
            return 13
        elif self.rank.isalnum():
            return self.rank
        
class Hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        pass
        
    def remove_card(self, card):
        pass

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
cards = []

player1_hand.add_card(card_one)
cards = [card_one]

player1_hand.add_card(card_two)
cards = [card_one, card_two]

player1_hand.remove_card(card_one)
cards = [card_two]