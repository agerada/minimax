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
initial_node = Node(board)
mcts.run_itt(initial_node)

# Check that the initial node (and its children are now in  
# nodes_and_chldn  
assert initial_node in mcts.nodes_and_chldn.keys()
assert mcts.nodes_and_chldn[initial_node] == initial_node.find_children()