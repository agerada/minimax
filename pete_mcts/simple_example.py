import numpy as np
from numpy.random import randint
from MCTS_Class import MCTS

"""
Testing script for MCTS class. Here we play the simple game:

            0
           / \
          /   \
         1     2
        / \   / \
       3   4 5   6

which has rewards:

State  Reward
-------------
3      1
4      2
5      0
6      1

"""

# Initiate generic MCTS
mcts = MCTS()

# Define simple game
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
                # If no more children then return the leaf node
                return node

def find_reward(node):

            if node == 3:
                reward = 1
            if node == 4:
                reward = 2
            if node == 5:
                reward = 0
            if node == 6:
                reward = 1

            return reward

# Assign rules of the game to mcts instance
mcts.find_children = find_children
mcts.random_sim = random_sim
mcts.find_reward = find_reward

# Choice 1
for i in range(1000):
    mcts.run_itt(node=0)
best_node = mcts.choose_move(node=0)
print('best first choice = node', best_node)

# Choice 2
for i in range(1000):
    mcts.run_itt(node=best_node)
best_node = mcts.choose_move(node=best_node)
print('best second choice = node', best_node)