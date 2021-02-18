from mcts import mcts, Knowledge
from tictactoe import initial_state, result, terminal, winner, minimax, player
import pickle, sys, os

sys.setrecursionlimit(1000)

ITERATIONS = 100
RESET_KNOWLEDGE = False

if RESET_KNOWLEDGE: 
    # generate base knowledge for X
    print('Resetting knowledge..')
    knowledge = Knowledge(ITERATIONS, 'X')

if not os.path.exists('knowledge.pkl'): 
    # generate base knowledge for X
    print('No previous knowledge found, generating base knowledge..')
    knowledge = Knowledge(ITERATIONS, 'X')
else: 
    with open('knowledge.pkl', 'rb') as input_knowledge: 
        print("Loading knowledge from knowledge.pkl..")
        knowledge = pickle.load(input_knowledge)


def quick_compare_mcts_minimax(runs = 1, knowledge = knowledge, test_minimax = False): 
    print('MCTS: ')
    print('\t(MCTS is player X)')
    print('\t(Minimax is player O)')
    for _ in range(runs): 
        board = initial_state()

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

    with open('knowledge.pkl', 'wb') as output_knowledge: 
        print("Saving knowledge to knowledge.pkl..")
        pickle.dump(knowledge, output_knowledge, pickle.HIGHEST_PROTOCOL)
        
    if not test_minimax: 
        return
    else: 
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