import tictactoe as ttt
import numpy as np
from numpy.random import randint


class Node():

    def __init__(self, board):
        self.board = board

    def find_children(self):
        moves = ttt.actions(self.board)
        children = []
        for m in moves:
            children.append(ttt.result(self.board, m))
        return children

class MCTS():

    def __init__(self):

        # Dictionary with node states as keys and children as items.
        self.nodes_and_chldn = dict()

        # Dictionary with node states as keys and no. visits as items.
        self.N = dict()

        # Dictionary with node states as keys and rewards as items.
        self.rewards = ()

    def run_itt(self, node):
        """ Runs a MCTS iteration starting from state defined by node.

        """

        # Check to see if we have visited state before
        visited = self.visited_before(node)

        # If we have visited the node before... (need to finish)
        if visited:
            pass

        # If we haven't visited the node before, then rollout from
        # here to the end of the game
        if not visited:
            reward = self.rollout(node)

    def visited_before(self, node):
        """ Returns true of node has been visited before (as parent)
            and false otherwise. If node hasn't been visited before
            then we find it's children and add it to nodes_and_chldn.
        """

        if node in self.nodes_and_chldn:
            return True
        else:
            self.find_children(node)
            return False


    def find_children(self, node):
        """ Finds children of node, and adds node to the nodes_and_chldn dictionary.

        """

        children = node.find_children()
        self.nodes_and_chldn[node] = children


    def rollout(self, node):
        """ Randomly plays from the state defined by node until
        the end of the game, returning the final outcome.

        """

        # Available moves from this point
        board = node.board
        moves = ttt.actions(board)

        # Used to store the winner
        w = None

        # Play until there's a winner
        while w is None:

            # Pick a random move
            n = randint(low=0, high=len(moves))
            action = moves[n]

            # Update the board (result automatically checks
            # whose go it is)
            board = ttt.result(board, action)

            # List all possible moves
            moves = ttt.actions(board)

            # See if anyone has won
            w = ttt.winner(board)

            # Break if we've run out of moves
            if len(moves) == 0:
                break

        if w is 'O':
            reward = 2
        elif w is None:
            reward = 1
        elif w is 'X':
            reward = 0

        return reward













