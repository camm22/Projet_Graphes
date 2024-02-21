
class Node:

    """
    This is the class that stores each attribute of each node. So the graph is made up of object nodes. This makes it
    easy to access the attributes of each node in the graph, such as duration and successors.
    """

    def __init__(self, name, duration):

        """The constructor of the Node class stores all its important attributes."""

        self.name = name  # Stores node's name
        self.duration = duration  # Stores node's duration
        self.edges = {}  # Stores the edges off the node : edges = {'1': '-', '2': self.duration, ...}
        self.object_edges = {}

    def initializeNode(self, nodes):

        """
        Initialize the dictionary edges of the node with default value.

        :param: nodes: list: contains the nodes of the graph
        """

        for node in nodes:
            self.edges[node] = '*'
            self.object_edges[node] = None
