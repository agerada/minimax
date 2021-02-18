import numpy as np
from abc import abstractmethod
from numpy.random import randint

class MCTS():

    def __init__(self):

        # Dictionary with node states as keys and children as items.
        self.nodes_and_chldn = dict()

        # Dictionary with node states as keys and no. visits as items.
        self.N = dict()

        # Dictionary with node states as keys and rewards below said
        # node as items.
        self.rewards = dict()


    @abstractmethod
    def find_children(self, node):
        """ Find and return all child states of the node.

        """
        pass

    @abstractmethod
    def random_sim(self, node):
        """ Simulate randomly from current state to the end
            of the game before then reporting the reward.

        """
        pass


    def run_itt(self, node):
        """ Runs a MCTS iteration starting from state defined by node.

        """

        # Start 'path', the list of nodes we visit before finding a
        # parent node that we haven't visited before.
        path = []

        while True:
            path.append(node)

            # Check to see if we have visited state before
            visited = node in self.nodes_and_chldn

            if visited:
                # If we have visited the node before then either move on to
                # (random) unvisited child or pick next node according to 
                # the UCT values of the children. 

                # Create list of children we haven't visited
                children = self.find_children(node)
                children_not_visited = list(set(children) - 
                                            set(self.nodes_and_chldn.keys()))
                                            
                if len(children_not_visited) > 0:
                    # If we have unvisited children, pick one at random
                    
                    i = randint(low = len(children_not_visited))
                    node = children_not_visited[i]
                else:
                    ## Need to finish
                    pass


            if not visited:
                # If we haven't visited the node as a parent before then we
                # its children, add to the dictionary of visited nodes and
                # perform a rollout. Also add it to the dictionaries that
                # record no. times visited and rewards.

                children = self.find_children(node)

                self.nodes_and_chldn[node] = children
                self.N[node] = 0
                self.rewards[node] = 0

                reward = self.random_sim(node)
                self.backprop(path, reward)
                
                break

    def backprop(self, path, reward):
        for node in path:
            self.N[node] += 1
            self.rewards[node] += reward










