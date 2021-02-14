from numpy.lib.polynomial import roots
from tictactoe import initial_state, player, actions, result, winner, terminal, utility
from numpy import log 
from math import sqrt, inf
from random import randrange

class Node(): 
    def __init__(self, action, parent, n = 0, t = 0):
        self.action = action
        self.parent = parent
        self.children = []
        self.n = 0
        self.t = 0
        self.ucb1 = inf
    
    def score(self): 
        """
        Update and return UCB1 score
        """
        self.ucb1 = self.t + (2 * sqrt(log(self.parent.n) / self.n))
        return self.ucb1
    
def simulation(board, action): 
    """
    Play out random simulations until terminal state reached
    Return +1 if X winner
    Return -1 if O winner
    Return 0 if tie
    """

    board = result(board, action)

    if terminal(board): 
        sim_winner = winner(board)
        if sim_winner == 'X': 
            return 1
        elif sim_winner == 'O': 
            return -1
        else: 
            return 0
    
    else: 
        moves = list(actions(board)) # converting to list for random subset
        rand_move = moves[randrange(0, len(moves))]
        return simulation(board, rand_move)

board =     [['O', None, 'X'],      # test board state
            [None, 'X', None],
            ['O', 'X', None]]

root_state = Node(action = None, parent = None)

for action in actions(board): 
    node = Node(action, root_state)
    root_state.children.append(node)

# test, for this board state, go through each possible action and simulate 
# 100 playout, return average 

for node in root_state.children: 
    sim = 0
    for i in range(0,100): 
        sim += simulation(board, node.action)
    print(node.action, sim)