import numpy as np
from numpy.random import randint
from abc import ABC, abstractmethod


class Node():

    def __init__(self, state):
        self.state = state

    @abstractmethod
    def find_children(self):
        """ Find and return all child states of the node.

        """
        pass


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

        # Start 'path', the list of nodes we visit before finding a
        # parent node that we haven't visited before.
        path = []
        path.append(node)

        # Check to see if we have visited state before
        visited = node in self.nodes_and_chldn

        if visited:
            # If we have visited the node before...
            ##(need to finish)
            pass

        if not visited:
            # If we haven't visited the node as a parent before then we
            # its children, add to the dictionary of visited nodes and
            # perform a rollout.

            children = node.find_children()
            self.nodes_and_chldn[node] = children
            self.rollout(node)
            self.backprop(node)

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













