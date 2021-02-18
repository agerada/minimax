import numpy as np
from abc import abstractmethod
from numpy.random import randint

class MCTS():

    """
    Description
    -----------
        A base class for Monte Carlo tree search algorithm.

    """

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
        """
        Description
        ------------
            Finds children of node and returns as a list. Is equal to
            'None' if the node has no children.
        """

        pass

    @abstractmethod
    def random_sim(self, node):
        """
        Description
        -----------
            Simulate randomly from current state, node,  to the end
            of the game. Returns the leaf node where it eventually
            finishes the game.

        """
        pass

    @abstractmethod
    def find_reward(self, node):
        """
        Description
        -----------
            Returns the reward associated with a leaf node.

        """
        pass

    def run_itt(self, node):
        """
        Description
        -----------
            Runs a MCTS iteration starting from state defined by node.

        Parameters
        ----------
            node : current state

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
                # the UCT values of the children. In other words, we move
                # down one layer in the tree.

                # Create list of children we haven't visited
                children = self.find_children(node)
                children_not_visited = list(set(children) -
                                            set(self.nodes_and_chldn.keys()))

                if len(children_not_visited) > 0:
                    # If we have unvisited children, pick one at random

                    i = randint(low = len(children_not_visited))
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
                # its children, add to the dictionary of visited nodes and
                # perform a rollout. Also add it to the dictionaries that
                # record no. times visited and rewards.

                children = self.find_children(node)

                self.nodes_and_chldn[node] = children
                self.N[node] = 0
                self.rewards[node] = 0

                leaf = self.random_sim(node)
                reward = self.find_reward(leaf)
                self.backprop(path, reward, leaf)

                break

    def backprop(self, path, reward, leaf):
        """
        Description
        -----------
            Takes the result of a rollout and back-propagates it
            back through the network.

        Parameters
        ----------
            path : list of nodes showing the route that we took to
                the leaf node. Note that it does not include the
                leaf node itself.

            reward : the reward associated with this particular
                rollout.

            leaf : the leaf node i.e. where we finally ended up at
                the end of the game.

        """

        # Back propagate the nodes in the path
        for node in path:
            self.N[node] += 1
            self.rewards[node] += reward


        if leaf not in self.N:
            # If we haven't seen this leaf node before, add it to
            # the N and rewards dictionaries
            self.N[leaf] = 0
            self.rewards[leaf] = 0

        # Update no. times visited and reward for leaf node
        self.N[leaf] += 1
        self.rewards[leaf] += reward

    def find_uct_values(self, parent, children):
        """
        Description
        -----------
            Find the utc values associated with a list of children nodes.
            We use this to help us choose which node to move to next (if
            all children have already been visited before).

        Parameters
        ----------
            parent : parent of all the child nodes that we're considering
                moving to

            children : list of child nodes

        Returns
        -------
            utc : numpy array of utc values associated with each node in
                children
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
            Chooses the next move that would maximise the estimated
            expected reward.

        Parameters
        ----------
            node : current state

        Returns
        -------
            best_node : the child node that has the maximum estimated
                expected reward.

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
