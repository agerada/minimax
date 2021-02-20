from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax
from numpy import log 
from math import sqrt, inf
from random import randrange

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
            self.ucb1 = (self.t / self.n) + (sqrt(2) * sqrt(log(self.parent.n) / self.n))
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
    
class Knowledge(): 
    def __init__(self, iterations, player): 
        board = initial_state()

        self.player = player
        self.root_state = Node(action = None, parent = None, board = board)

        for action in actions(board): 
            node = Node(action, self.root_state, board)
            self.root_state.children.append(node)
        for _ in range(iterations): 
            nd = selection(self.root_state)
            expansion(nd, player)

        # create save state (always defaults to root node on creation)
        # used to efficiently start search
        self.save_state = self.root_state

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
            return 1
        else: 
            return 0
    
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

def expansion(node, current_player): 
        # check for terminal board (no sim or expansion needed) 
    if terminal(node.resulting_state): 
        if winner(node.resulting_state) == current_player: 
            temp_t = 1
            node.t += 1
        elif winner(node.resulting_state) == None: 
            temp_t = 1
            node.t += 1
        else: 
            temp_t = 0
            node.t += 0
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

def mcts(board, iterations, knowledge): 
    """
    Return optimal move using MCTS algorithm
    Iterations is the number of times to run MCTS
    """

    current_player = player(board)

    if board == initial_state(): 
        # if blank board, then start at root node
        # no need to select and expand node as already done at __init__
        # of knowledge
        nd = knowledge.root_state
    else: 
        # otherwise find working node by searching through states in tree
        nd = search_node(board, knowledge.save_state)
        if not nd: 
            raise NotImplementedError # don't know how to deal with unseen moves yet
        for _ in range(iterations): 
            temp_selection_node = selection(nd)
            expansion(temp_selection_node, current_player)

    # Check for winning moves
    for move in nd.children: 
        if move.is_terminal_move(board): 
            if move.outcome == current_player: 
                # no need to save state as game is ending
                return move.action

    # Find node with highest t per n
    max_node = max(nd.children, key= lambda x: x.t / x.n)
    # save state
    knowledge.save_state = max_node
    return max_node.action

def search_node(state, node): 
  if node.resulting_state == state: 
    return node
  for child in node.children: 
    n = search_node(state, child)
    if n: 
      return n
  return None