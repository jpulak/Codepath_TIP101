#Problem 8: Get Rank
'''The Player class has been updated below with a new attribute ahead to represent the player currently directly ahead of them in the race.

Write a function get_rank() that accepts a Player object my_player and returns their current place number in the race.

class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
        
def get_place(my_player):
	pass
Example Usage:

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
print(player1_rank)

player2_rank = get_place(peach)
print(player2_rank)

player3_rank = get_place(mario)
print(player3_rank)
Example Output:

3
1
2'''