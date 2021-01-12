from tictactoe import player, actions, terminal, winner, utility

EMPTY = None

def result(board, action):
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

board =     [['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', None]]

print(utility(board))