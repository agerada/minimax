from numpy.lib.polynomial import roots
from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax
from numpy import log 
from math import sqrt, inf
from random import randrange
import sys

class Node(): 
    def __init__(self, action, parent, board, n = 0, t = 0):
        self.action = action
        self.parent = parent
        self.children = []
        self.n = 0
        self.t = 0
        self.ucb1 = inf
        self.terminal = False
        self.outcome = None

        self.original_state = board # board state pre-action
        if not action: # initial state root node
          self.resulting_state = None
        else: 
          self.resulting_state = result(board, action) # board state after action
    
    def score(self): 
        """
        Update and return UCB1 score
        """
        if self.n == 0: 
            self.ucb1 = inf
            return self.ucb1
        else: 
            self.ucb1 = (self.t / self.n) + (2 * sqrt(log(self.parent.n) / self.n))
            return self.ucb1

    def is_terminal_move(self, board): 
        """
        Check whether this Node leads immediately to an end state
        """
        board_result = result(board, self.action)
        if terminal(board_result):
            self.terminal = True
            self.outcome = winner(board_result)
            return self.terminal
        else: 
            return False
    
def simulation(board, action, current_player): 
    """
    Play out random simulations until terminal state reached
    Return +1 if X winner
    Return -1 if O winner
    Return 0 if tie
    """
    board = result(board, action)

    if terminal(board):  
        sim_winner = winner(board)
        if sim_winner == current_player: 
            return 1
        elif sim_winner == None: 
            return 0
        else: 
            return -1
    
    else: 
        moves = list(actions(board)) # converting to list for random subset
        rand_move = moves[randrange(0, len(moves))]
        return simulation(board, rand_move, current_player)

def selection(node): 
    """
    Recursive function that traverses tree until find max score leaf node and return it
    If more than 1 leaf node, return random one
    """
    if not node.children:     # leaf node
        return node
    else: 
        max_score = 0
        max_nodes = []
        for child_node in node.children: 
            score = child_node.score()
            if score > max_score or not max_score: 
                max_score = score
                max_nodes = [child_node]
            elif score == max_score: 
                max_nodes.append(child_node)
        if len(max_nodes) == 1: 
            return selection(max_nodes[0])
        else: 
            rand_num = randrange(0,len(max_nodes))
            return selection(max_nodes[rand_num])

def expansion(node, board, current_player): 
        # check for terminal board (no sim or expansion needed) 
    if terminal(node.resulting_state): 
        if winner(node.resulting_state) == current_player: 
            temp_t = 1
            node.t += 1
        elif winner(node.resulting_state) == None: 
            temp_t = 1
            node.t += 1
        else: 
            temp_t = -1
            node.t += -1
        node.n += 1
        temp_node = node
        while temp_node.parent: 
            temp_node = temp_node.parent
            temp_node.t += temp_t
            temp_node.n += 1

    if node.n == 0: 

        # conduct sim (non visited node)
            sim_score = simulation(node.original_state, node.action, current_player)
            node.t += sim_score
            node.n += 1

        # backpropogation 
            temp_node = node
            while temp_node.parent: 
                temp_node = temp_node.parent
                temp_node.t += sim_score
                temp_node.n += 1
                
    elif not terminal(node.resulting_state): 
        # expand node
        for action in actions(node.resulting_state): 
            child_node = Node(action, parent = node, board = node.resulting_state)
            node.children.append(child_node)

def mcts(board, iterations): 
    """
    Return optimal move using MCTS algorithm
    Iterations is the number of times to run MCTS
    """
    current_player = player(board)

    root_state = Node(action = None, parent = None, board = board)
    for action in actions(board): 
        node = Node(action, root_state, board)
        root_state.children.append(node)

    for _ in range(iterations): 
        nd = selection(root_state)
        expansion(nd, board, current_player)
    
    # Check for winning moves
    for move in root_state.children: 
        if move.is_terminal_move(board): 
            if move.outcome == current_player: 
                return move.action

    return(max(root_state.children, key= lambda x: x.t).action)

