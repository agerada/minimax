import numpy as np
from MCTS_Class import MCTS
import sys
sys.path.append('..')
import tictactoe as ttt
from numpy.random import randint

"""
Description ...
"""

# Initiate generic MCTS
mcts = MCTS()

# Define game
def find_children(node):

    actions = ttt.actions(node)
    children = []
    for a in actions:
        children.append(ttt.result(node, a))

    return children

def random_sim(node):
    winner = None
    while winner is None:
        actions = ttt.actions(node)
        if len(actions) == 0:
            break
        i = randint(low=len(actions))
        node = ttt.result(node, actions[i])
        winner = ttt.winner(node)

    return node

def find_reward(node):
    winner = ttt.winner(node)
    if winner == 'X':
        reward = 2
    if winner is None:
        reward = 1
    if winner == 'O':
        reward = 0

    return reward

class Node:
    def __init__(self, board):
        self.board = board

# Assign rules of the game to mcts instance
mcts.find_children = find_children
mcts.random_sim = random_sim
mcts.find_reward = find_reward

# Initialise the game
board = ttt.initial_state()

# First run 
mcts.run_itt(node)
best_node = mcts.choose_move(node)
