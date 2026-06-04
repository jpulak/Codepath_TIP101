#Problem 6: Rock, Paper, Scissors
'''Write a function rock_paper_scissors() that determines 
the winner of a game of Rock, Paper, Scissors.
 The function accepts two strings as parameters: player1 and 
 player2. Each parameter can have a value of "rock", "paper",
   or "scissors".

Print either "Player 1 wins!" or "Player 2 wins!" 
according to the following rules:
Rock wins against scissors.
Scissors wins against paper.
Paper wins against rock.

If both player1 and player2 have the same value, print 
"It's a tie!".

def rock_paper_scissors(player1, player2):
    pass
Example Usage:

rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")
Example Output:

It's a tie!
Player 2 wins!
Player 1 wins!
Player 2 wins!
Player 1 wins!'''

def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif player2 == "rock":
        if player1 == "scissors":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    elif player2 == "paper":
        if player1 == "rock":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    elif player2 == "scissors":
        if player1 == "paper":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")