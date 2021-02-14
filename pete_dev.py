import tictactoe as ttt
import numpy as np
from numpy.random import randint

"""
Some random players playing against each other, so Pete can
understand what's going on.

"""

# Initialise with a blank board
board = ttt.initial_state()

# Initial moves
moves = ttt.actions(board)

# Used to store the winner
w = None

# Play until there's a winner
while w is None:

    # Pick a random move
    n = randint(low=0, high=len(moves))
    action = moves[n]

    # Update the board (result automatically checks
    # whose go it is)
    board = ttt.result(board, action)
    
    # List all possible moves
    moves = ttt.actions(board)

    # See if anyone has won
    w = ttt.winner(board)
    
    # Break if we've run out of moves
    if len(moves) == 0:
        break

print('Winner is ', w, '\n')
[print(i) for i in board]
