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

# Fix random seed so that we run same test each time
np.random.seed(42)

# Run first iteration and check that the nodes dictionaries are
# what we would expect.
mcts.run_itt(node=0)
assert mcts.nodes_and_chldn == dict({0 : [1,2]})
assert mcts.N == dict({0 : 1})
assert mcts.rewards == dict({0 : 2})

# On the second iteration (with random seed fixed) it should rollout
# from node 1. This means that nodes 0 and 1 have been visited twice and
# once respectively. 
mcts.run_itt(node=0)
assert mcts.nodes_and_chldn == {0: [1, 2], 1: [3, 4]}
assert mcts.N == {0: 2, 1: 1}

# On the third iteration (with random seed fixed) rollout has to be conducted
# from node 2. 
mcts.run_itt(node=0)
assert mcts.nodes_and_chldn == {0: [1, 2], 1: [3, 4], 2: [5, 6]}

# On the fourth iteration we should pick the node with the largest 
# uct value and then rollout from one of its children. We are now hitting
# leaf nodes so the dictionary of visited nodes should remain the same.
mcts.run_itt(node=0)
assert mcts.nodes_and_chldn == {0: [1, 2], 1: [3, 4], 2: [5, 6]}



