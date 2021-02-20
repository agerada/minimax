import numpy as np
from numpy.random import randint
from MCTS_Class import MCTS_Base, Node_Base

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

    def is_terminal(self):

        if self.state == 3:
            self.terminal = True
            reward = 1
        elif self.state == 4:
            self.terminal = True
            self.reward = 2
        elif self.state == 5:
            self.terminal = True
            self.reward = 0
        elif self.state == 6:
            self.terminal = True
            self.reward = 1
        else:
            self.terminal = False


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

class MCTS(MCTS_Base):

    def random_sim(self, node):

        while node.chld_states is not None:

            if node.chld_states is not None:
                # If there are children, then pick one at random as the
                # new node
                i = randint(low=len(node.chld_states))
                node = Node(state=node.chld_states[i])
                
                if node.terminal:                    
                    # Return if terminal node
                    return node

# Initiate MCTS instance
mcts = MCTS()


## Test first iteration

# Fix random seed so that we run same test each time
np.random.seed(42)

# Run first iteration and check that the nodes and leaf nodes visited
# are what we would expect
node = Node(state=0)
mcts.run_itt(node)
assert mcts.visited_nodes[0].state == 0
assert mcts.visited_nodes[0].N == 1
assert mcts.visited_nodes[0].Q == 2
assert mcts.visited_leaf_nodes[0].state == 4
assert mcts.visited_leaf_nodes[0].N == 1
assert mcts.visited_leaf_nodes[0].Q == 2

# On the second iteration should roll our from a node on the second layer.
##mcts.run_itt(node)

'''
def test_itt2():
    # On the second iteration (with random seed fixed) it should rollout
    # from node 1. This means that nodes 0 and 1 have been visited twice and
    # once respectively.
    mcts.run_itt(node=0)
    assert mcts.nodes_and_chldn == {0: [1, 2], 1: [3, 4]}
    assert mcts.N == {0: 2, 4: 1, 1: 1, 3: 1}


def test_itt3():
    # On the third iteration (with random seed fixed) rollout has to be
    # conducted from node 2.
    mcts.run_itt(node=0)
    assert mcts.nodes_and_chldn == {0: [1, 2], 1: [3, 4], 2: [5, 6]}


def test_itt4():
    # On the fourth iteration we should pick the node with the largest
    # uct value and then rollout from one of its children. We are now hitting
    # leaf nodes so the dictionary of visited nodes should remain the same.
    mcts.run_itt(node=0)
    assert mcts.nodes_and_chldn == {0: [1, 2], 1: [3, 4], 2: [5, 6]}


def test_monte_calro():
    # Now if we run it lots of times, the expected reward associated with
    # node 1 should converge to 1.5
    for i in range(1000):
        mcts.run_itt(node=0)
    assert np.allclose(mcts.rewards[1] / mcts.N[1], 1.5, atol=0.01)

    # Check that it chooses node 1 on the first move
    best_node = mcts.choose_move(node=0)
    assert best_node == 1

    # Check that it chooses node 4 on the second move
    for i in range(1000):
        mcts.run_itt(node=best_node)
    best_node = mcts.choose_move(node=best_node)
    assert best_node == 4
'''
