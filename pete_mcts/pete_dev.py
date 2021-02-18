import numpy as np
from numpy.random import randint
from MCTS_Class import MCTS

"""
Dev script for MCTS class.

"""

# Initiate generic MCTS
mcts = MCTS()

# Define a simple game for testing purposes
def find_children(node):

    if node == 0:
        children = [1, 2]
    if node == 1:
        children = [3, 4]
    if node == 2:
        children = [5, 6]
    if node in [3, 4, 5, 6]:
        children = None

    return children

def random_sim(node):

    children = mcts.find_children(node)
    while children is not None:

        if children is not None:
            # If there are children, then pick one at random as the
            # new node
            i = randint(low = len(children))
            node = children[i]
            children = mcts.find_children(node)

        if children is None:
            # If no more children then return the reward
            if node == 3:
                reward = 1
            if node == 4:
                reward = 2
            if node == 5:
                reward = 1
            if node == 6:
                reward = 0

            return reward



# Assign rules of the game to mcts instance
mcts.find_children = find_children
mcts.random_sim = random_sim

# Run first iteration and check that the nodes and children dictionary
# is correct. 
mcts.run_itt(node=0)
assert mcts.nodes_and_chldn == dict({0 : [1,2]})

