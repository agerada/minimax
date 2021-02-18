from mcts import *

board =     [['O', None, 'X'],      # test board state
            [None, 'X', None],
            ['O', 'X', None]]

sys.setrecursionlimit(10000)

ITERATIONS = 100

knowledge = Knowledge(ITERATIONS, 'X')

def quick_compare_mcts_minimax(runs = 10, knowledge = knowledge): 
    print('MCTS: ')
    print('\t(MCTS is player X)')
    print('\t(Minimax is player O)')
    for _ in range(runs): 
        board = initial_state()

        # generate base knowledge for X

        # MCTS is X and makes first move

        board = result(board, mcts(board, ITERATIONS, knowledge))

        # Play until there's a winner
        while not terminal(board):

            # Make a move
            if player(board) == 'X': 
                board = result(board, mcts(board, ITERATIONS, knowledge))
            else: 
                board = result(board, minimax(board))

        outcome = winner(board)

        if outcome == 'X': 
            print('Player X is winner')
        elif outcome == 'O': 
            print('Player O is winner')
        else: 
            print('Tie')

    print('Minimax only: ')
    for _ in range(runs): 
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
    
quick_compare_mcts_minimax()