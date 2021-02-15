from mcts import *

board =     [['O', None, 'X'],      # test board state
            [None, 'X', None],
            ['O', 'X', None]]

sys.setrecursionlimit(10000)

ITERATIONS = 1000

for _ in range(10): 
    board =     [['O', None, 'X'],      # test board state
                [None, None, None],
                [None, 'X', None]]
    board = initial_state()

    # MCTS is X and makes first move

    board = result(board, mcts(board, ITERATIONS))

    # Play until there's a winner
    while not terminal(board):

        # Make a move
        if player(board) == 'X': 
            board = result(board, mcts(board, ITERATIONS))
        else: 
            board = result(board, minimax(board))

    outcome = winner(board)

    if outcome == 'X': 
        print('Player X is winner')
    elif outcome == 'O': 
        print('Player O is winner')
    else: 
        print('Tie')

"""
print('Minimax: ')

for i in range(2): 
    board = initial_state()

    while not terminal(board): 
        board = result(board, minimax(board))

    outcome = winner(board)

    if outcome == 'X': 
        print('Player X is winner')
    elif outcome == 'O': 
        print('Player O is winner')
    else: 
        print('Tie')
"""