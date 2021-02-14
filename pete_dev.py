import tictactoe as ttt
import numpy as np
from numpy.random import randint

"""
Some random players playing against each other, so Pete can 
understand what's going on. 

"""

# Initialise with a blank board
board = ttt.initial_state()

# Used to store the winner
w = None

# Play until there's a winner
while w is None:

    # List all possible moves
    moves = list(ttt.actions(board))
    
    # Pick a random move
    n = randint(low=0, high=len(moves))
    action = moves[n]
    
    # Update the board (result automatically checks
    # whose go it is)
    board = ttt.result(board, action)
    
    # See if anyone has won 
    w = ttt.winner(board)

print('Winner is ', w, '\n')
[print(i) for i in board]
