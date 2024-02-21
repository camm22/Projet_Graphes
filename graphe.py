from fonctions import *
from node import *
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    """
    The Graph class is the program's main structure. It stores in memory and manages all the different graphs read from
    txt files, thanks to its attributes, which give easy access to all the important characteristics of the graph,
    and its methods, which enable it to be executed.
    """

    def __init__(self):

        """The constructor of the graph class stores all its important attributes."""

        self.nb_node = 0  # Stores graph's order.
        self.nodes = []  # Stores node in a list  : nodes = ['1', '2', ...].
        self.nb_edge = 0  # Stores the number of edges contained in the graph.
        self.edges = []  # Stores the different edges i a list : edges = ['1;2;2', ...] -> node;duration;successor.

        self.max_length_node = 0  # Stores the maximum number of characters in the name of different nodes.
        self.max_length_duration = 0  # Stores the maximum number of characters in the duration of different nodes.
        self.max_length_case = 0  # Stores the maximum between max_length_node and max_length_duration.

        self.list_node_object = []  # Stores the different Object Node : list_node_object = [<Node1>, <Node2>, ...].

        self.list_graph_file = []  # Stores the different lines contents of the read txt file.

    def showGraph(self):
        G = nx.Graph()
        for node in self.list_node_object:
            G.add_node(node.name)
            for key, value in node.edges.items():
                if value != '*':
                    G.add_edge(node.name, key)
        nx.draw(G, node_size=100, node_color='r', with_labels=True, font_size=5, width=2.0)
        plt.draw()

    def doesGraphHaveCircuit(self, power):
        pass

    def areEdgesPositive(self, power):

        """
        To verify if there is at least one edge with an negative value.
        Creation of a list containing the negative edges.

        :param: power: boolean: to display information
        :return: boolean: if one Edges is positive or negative
        """

        very = False
        edges = []
        for node in self.list_node_object:
            if node.duration < 0:
                very = True
                for key, value in node.edges.items():
                    if value != '*':
                        edges.append(node.name + '-(' + str(node.duration) + ')->' + key)
        if power:
            displayInfoAreEdgesPositive(very, edges)

        return very

    def space(self, length_char):

        """
        Computes the space after each char in each cell of the value matrix.

        :return: str: Which contains between 2 and n ' '.
        """

        return ' ' * (self.max_length_case - length_char)

    def displayGraph(self):

        """
        Display the value matrix of the graph.
        """

        print(white + bold + ' '*self.max_length_case, end=' ')

        for node in self.nodes:
            print(' |' + node + self.space(len(node)), end=' ')

        print()

        # Print the first line.

        for i in range(len(self.list_node_object)):
            print(self.list_node_object[i].name + self.space(len(self.list_node_object[i].name)), end=' ')

            for key, value in self.list_node_object[i].edges.items():
                print(' |' + str(value) + self.space(len(str(value))), end=' ')

            if i + 1 == len(self.list_node_object):
                print(normal)
            else:
                print()

        # Print the first column with the content of the matrix.

    def maxLengthNode(self):

        """
        Computes the maximum number of characters in the name of different nodes.

        :return: int: the maximum number of characters in the name of different nodes.
        """

        l = []
        for node in self.nodes:
            l.append(len(node))
        if len(l) == 0:
            return 1
        return max(l)

    def maxLengthDuration(self):

        """
        Computes the maximum number of characters in the duration of different nodes.

        :return: int: the maximum number of characters in the duration of different nodes.
        """

        l = []
        for node in self.list_node_object:
            for key, value in node.edges.items():
                l.append(value)
        if len(l) == 0:
            return 1
        for i in range(len(l)):
            l[i] = len(str(l[i]))
        return max(l)

    def initializeGraph(self):

        """
        Loads the graph into memory, assigning the correct data to each graph attribute from the list of lines in
        the txt file contained in self.list_graph_file .
        """

        node_with_successor = []

        self.nodes.append('0')
        self.list_node_object.append(Node('0', 0))

        # Add the alpha node.

        for line in self.list_graph_file:
            my_list = line.split(' ')
            self.nodes.append(my_list[0])
            self.list_node_object.append(Node(my_list[0], int(my_list[1])))

        # Initializes all the nodes and the Nodes Object and adds it to the appropriate lists.

        for line in self.list_graph_file:
            my_list = line.split(' ')

            if len(my_list) == 2:
                self.edges.append('0;0;' + my_list[0])
                node_with_successor.append('0')
            else:
                for i in range(2, len(my_list)):
                    for node in self.list_node_object:
                        if my_list[i] == node.name:
                            self.edges.append(my_list[i] + ';' + str(node.duration) + ';' + my_list[0])
                            node_with_successor.append(my_list[i])

        # Updates self.edges .

        node_with_successor = list(set(node_with_successor))
        omega = str(len(self.nodes))
        omega_node = Node(omega, 0)

        # Checking nodes with successor and creating the omega node.

        for node in self.list_node_object:
            if node.name not in node_with_successor:
                self.edges.append(node.name + ';' + str(node.duration) + ';' + omega)

        # Added new edges that lead nodes without successors to omega.

        self.nodes.append(omega)
        self.list_node_object.append(omega_node)
        self.nb_node = len(self.nodes)
        self.nb_edge = len(self.edges)

        # Updates attributes

        for node in self.list_node_object:
            node.initializeNode(self.nodes)

        # Initialize the edges dictionary of each Node Object.

        for edge in self.edges:
            edge = edge.split(';')
            for node in self.list_node_object:
                if edge[0] == node.name:
                    node.edges[edge[2]] = node.duration

        # Updates the edges dictionary values of each Node Object.

        self.max_length_node = self.maxLengthNode()
        self.max_length_duration = self.maxLengthDuration()
        self.max_length_case = max(self.max_length_node, self.max_length_duration, 2)

        # Updates other attributes.

    def readGraphFromFile(self, path):

        """
        Read the contents of the txt file which contains the graph data and call the initializeGraph() method.

        :param path: str : path of the txt file.
        """

        graph_file = open(path, 'r', encoding='utf-8')
        self.list_graph_file = graph_file.readlines()
        graph_file.close()

        for i in range(len(self.list_graph_file)):
            self.list_graph_file[i] = self.list_graph_file[i].strip('\n')

        # Initialize self.list_graph_file .

        self.initializeGraph()
