import numpy as np
from numpy.random import randint
from MCTS_Class import MCTS, Node_Base

"""
Here we play the simple game:

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


class Node(Node_Base):

    def find_chld_states(self):

        if self.state == 0:
            chld_states = [1, 2]
        if self.state == 1:
            chld_states = [3, 4]
        if self.state == 2:
            chld_states = [5, 6]
        if self.state in [3, 4, 5, 6]:
            chld_states = None

        return chld_states

    def random_sim(self):

        children = mcts.find_children(node)
        while children is not None:

            if children is not None:
                # If there are children, then pick one at random as the
                # new node
                i = randint(low=len(children))
                node = children[i]
                children = mcts.find_children(node)

                if children is None:
                    # If no more children then return the leaf node
                    return node

    def find_reward(self):

        if node == 3:
            reward = 1
        if node == 4:
            reward = 2
        if node == 5:
            reward = 0
        if node == 6:
            reward = 1

        return reward


node = Node(state=0)

# Initiate MCTS instance 
mcts = MCTS()


'''
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
'''