import tictactoe as ttt
import numpy as np
from numpy.random import randint


class MCTS():

    def __init__(self):

        # Dictionary with node states as keys and children as items. 
        self.nodes_and_chldn = dict()
        
        # Dictionary with node states as keys and no. visits as items. 
        self.N = dict()
        
        # Dictionary with node states as keys and rewards as items. 
        self.rewards = ()

    def visited_before(self, node):
        """ Returns true of node has been visited before (as parent)
            and false otherwise
        """

        pass
        
    def find_children(self, node):
        """ Finds children of node, and adds node to the nodes_and_chldn
            dictionary. 
        
        """
        
        pass
        
    def rollout(self, node):
        """ Randomly plays from the state defined by node until the end
            of the game, returning the final outcome. 
        
        """
        
        pass













