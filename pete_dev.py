import tictactoe as ttt
import numpy as np
from numpy.random import randint
from MCTS_Class import MCTS, Node

"""
Dev script for MCTS class (playing as 'O'). 

"""

mcts = MCTS()

# Initialise with a blank board and let player 1 make a 
# random move
board = ttt.initial_state()
moves = ttt.actions(board)
n = randint(low=0, high=len(moves))
action = moves[n]
board = ttt.result(board, action)

# First iteration of MCTS 
mcts.run_itt(Node(board))

