import numpy as np
from abc import abstractmethod, ABC
from numpy.random import randint

class Node_Base(ABC):

    """
    Description
    -----------

    """

    def __init__(self, state):
        self.state = state
        self.chld_states = self.find_chld_states()
        self.N = 0
        self.Q = 0
        self.is_terminal()

    @abstractmethod
    def is_terminal(self):
        pass

    @abstractmethod
    def find_chld_states(self):
        pass


class MCTS_Base(ABC):

    """
    Description
    -----------
        A base class for Monte Carlo tree search algorithm.

    """

    def __init__(self):

        self.visited_nodes = []
        self.visited_leaf_nodes = []

    @abstractmethod
    def random_sim(self, node):
        pass

    def run_itt(self, node):
        """
        Description
        -----------
            Runs a MCTS iteration starting from state defined by node.

        """

        # Start 'path', the list of nodes we visit before finding a
        # parent node that we haven't visited before.
        path = []

        while True:
            path.append(node)

            # Check to see if we have visited this state before
            visited = node in self.visited_nodes

            if visited:
                # If we have visited the node before then either move on to
                # (random) unvisited child or pick next node according to
                # the UCT values of the children. In other words, we move
                # down one layer in the tree.

                # Create list of children we haven't visited
                children = self.find_children(node)
                children_not_visited = list(set(children) -
                                            set(self.nodes_and_chldn.keys()))

                if len(children_not_visited) > 0:
                    # If we have unvisited children, pick one at random

                    i = randint(low=len(children_not_visited))
                    node = children_not_visited[i]
                else:
                    # If we have visited all children, pick the one with
                    # the largest UCT value
                    uct_values = self.find_uct_values(node, children)
                    i = np.where(uct_values == np.max(uct_values))[0][0]
                    node = children[i]

                if self.find_children(node) is None:
                    # If this is a terminal node then we don't need to
                    # add it nodes visited and do a rollout etc.

                    reward = self.find_reward(node)
                    self.backprop(path, reward, node)

                    break

            if not visited:
                # If we haven't visited the node as a parent before then we
                # perform a rollout from this point. We also add this node
                # to our list of visited nodes.

                self.visited_nodes.append(node)
                leaf_node = self.random_sim(node)
                self.backprop(path, leaf_node)

                break

    def backprop(self, path, leaf_node):
        """
        Description
        -----------

        """

        reward = leaf_node.reward

        # Back propagate the nodes in the path
        for node in path:
            node.N += 1
            node.Q += reward

        # See if we have visited this leaf node before
        visited_leaf_states = []
        for node in self.visited_leaf_nodes:
            visited_leaf_states.append(node.state)
        i = np.where(leaf_node.state == visited_leaf_states)[0]

        if len(i) == 0:
            # If we haven't seen this leaf node before, add it to
            # visited leaf states
            leaf_node.N += 1
            leaf_node.Q += reward
            self.visited_leaf_nodes.append(leaf_node)
        else:
            # Otherwise update statistics of the previously visited
            # leaf node
            self.visited_leaf_nodes[i].N += 1
            self.visited_leaf_nodes[i].Q += reward

    def find_uct_values(self, parent, children):
        """
        Description
        -----------

        """

        n_parent = self.N[parent]
        uct = np.array([])

        for node in children:

            # Extract no. times visited and total reward
            # 'underneath' the node.
            n_child = self.N[node]
            reward = self.rewards[node]

            # Estimate of expected reward
            EX = reward / n_child

            # Find uct
            uct = np.append(uct,
                            EX + 2 * np.sqrt(np.log(n_parent) / n_child))
        return uct

    def choose_move(self, node):
        """
        Description
        -----------


        """

        children = self.find_children(node)
        EX = np.array([])
        for node in children:
            n_child = self.N[node]
            reward = self.rewards[node]
            EX = np.append(EX, reward / n_child)

        i = np.where(EX == np.max(EX))[0][0]
        best_node = children[i]

        return best_node
