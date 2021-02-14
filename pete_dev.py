import tictactoe as ttt
import numpy as np
from numpy.random import randint

"""
Some random players playing against each other, so Pete can
understand what's going on.

"""

for n_MC in range(10):

    # Initialise with a blank board
    board = ttt.initial_state()

    # Initial moves
    moves = list(ttt.actions(board))

    # Used to store the winner
    w = None

    # Play until there's a winner
    while w is None or len(moves) > 0:

        # Pick a random move
        n = randint(low=0, high=len(moves))
        action = moves[n]

        # Update the board (result automatically checks
        # whose go it is)
        board = ttt.result(board, action)
        
        # List all possible moves
        moves = list(ttt.actions(board))

        # See if anyone has won
        w = ttt.winner(board)


    print('Winner is ', w, '\n')
##[print(i) for i in board]
