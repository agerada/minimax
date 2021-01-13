"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():    # TESTED - WORKING
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):      # TESTED - WORKING
    """
    Returns player who has the next turn on a board.
    """
    ## Unnest the matrix and return X if empty
    unnested = [item for sublist in board for item in sublist]
    if all([i == None for i in unnested]): 
        return 'X'
    
    ## otherwise sum each player and return next player
    else: 
        moves_x = sum([i == 'X' for i in unnested])
        moves_o = sum([i == 'O' for i in unnested])
        if moves_x > moves_o: 
            return 'O'
        else: 
            return 'X'

def actions(board):     # TESTED - WORKING
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for row in range(3): 
        for cell in range(3): 
            if board[row][cell] == None: 
                moves.add((row, cell))
    return moves

def result(board, action):  # TESTED - WORKING
    """
    Returns the board that results from making move (i, j) on the board.
    """
    ## Create deep copy by iterating through board
    ## note - this only works for a 3 x 3 board
    board_copy = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    for row in range(3): 
        for cell in range(3): 
            board_copy[row][cell] = board[row][cell]

    ## Check if action out of bounds
    if action[0] < 0 or action[0] > 2: 
        print('Index out of bounds')
        raise IndexError
    if action[1] < 0 or action[1] > 2: 
        print('Index out of bounds')
        raise IndexError

    ## Check if action over writes: 
    if board_copy[action[0]][action[1]] is not None: 
        print('Index overwrites action')
        raise ValueError
    
    ## Otherwise return deep copy with new action, 
    ## using player function to determine whether to add X or O
    board_copy[action[0]][action[1]] = player(board_copy)
    return board_copy

def winner(board):      # TESTED - WORKING 
    """
    Returns the winner of the game, if there is one.
    """

    x_winner = False
    o_winner = False

    ## Horizontal first
    for row in board: 
        if all([cell == 'X' for cell in row]): 
            x_winner = True
        if all([cell == 'O' for cell in row]): 
            o_winner = True

    ## Vertical
    for col in range(3): 
        if all([board[row][col] == 'X' for row in range(3)]): 
            x_winner = True
        if all([board[row][col] == 'O' for row in range(3)]): 
            o_winner = True

    ## Diagonal top left to bottom right
    if all([board[ind][ind] == 'X' for ind in range(3)]): 
        x_winner = True
    if all([board[ind][ind] == 'O' for ind in range(3)]): 
        o_winner = True

    ## Diagonal top right to bottom left 
    diag = [(0,2),(1,1),(2,0)]
    if all([board[ind[0]][ind[1]] == 'X' for ind in diag]): 
        x_winner = True
    if all([board[ind[0]][ind[1]] == 'O' for ind in diag]): 
        o_winner = True

    if x_winner and o_winner: 
        print('Board has both X and O winner')
        raise ValueError
    elif x_winner: 
        return 'X'
    elif o_winner: 
        return 'O'
    else: 
        return None

def terminal(board):    # TESTED - WORKING
    """
    Returns True if game is over, False otherwise.
    """

    ## Check for winner
    if winner(board) is not None: 
        return True

    ## Check if board full
    unnested = [item for sublist in board for item in sublist]
    if (all(i is not None for i in unnested)): 
        return True

    return False

def utility(board):     # TESTED - WORKING
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X': 
        return 1
    elif winner(board) == 'O':
        return -1
    else: 
        return 0

def min_value(board):   
    """
    recursive function (back and forth to max_value simulating each turn)
    returns the min value for board assuming each player
    plays optimally
    """
    if terminal(board): 
        return utility(board)
    v = math.inf
    for action in actions(board): 
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):   
    """
    recursive function (back and forth to min_value simulating each turn)
    returns the max value for board assuming each player
    plays optimally
    """
    if terminal(board): 
        return utility(board)
    v = -math.inf
    for action in actions(board): 
        v = max(v, min_value(result(board, action)))
    return v

def minimax(board):     
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == 'X': 
        moves_reviewed = {}
        for action in actions(board): 
            # what is the score of the board if opposite player plays optimally
            moves_reviewed[action] = min_value(result(board, action))
        return max(moves_reviewed, key = moves_reviewed.get)

    else: # player O
        moves_reviewed = {}
        for action in actions(board): 
            moves_reviewed[action] = max_value(result(board, action))
        return min(moves_reviewed, key = moves_reviewed.get)