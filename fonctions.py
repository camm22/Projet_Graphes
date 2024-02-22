import time


def displayInfoDoesGraphHaveCircuit(very):
    pass


def displayInfoAreEdgesPositive(very, edges):

    """
    Correctly displays negative arcs if any.

    :param: very: boolean: if one Edges is positive or negative.
    :param: edges: list: containing the negative edges.
    """

    nb = len(edges)
    final = '\n' + yellow + "   [•]" + normal

    if very:
        if nb > 1:
            adjective1 = "des arcs négatifs :"
        else:
            adjective1 = "un arc négatif :"

        final += "Ce graphe possède " + adjective1

        for edge in edges:
            final += ' |' + edge + '|'
        final += '.'
    else:
        final += "Ce graphe ne possède pas d'arc négatif."

    print(final)


def displayInfoInitializeGraph(graph):

    """
    Shows graph initialization information in memory.

    :param graph: Object Graph: graph instance in use.
    """

    i = 0

    pause(my_time_1)
    print(red + '{•} ' + normal + "Nombre de sommets : " + white + str(graph.nb_node))
    pause(my_time_05)
    print(red + '\n{•} ' + normal + "Sommets : " + white, end='')

    for node in graph.list_node_object:
        i += 1

        pause(my_time_03)
        print('(' + node.name + graph.space(len(node.name)) + ') ', end='')

        if i == 5:
            print('\n              ', end='')
            i = 0

    pause(my_time_05)
    print(red + '\n\n{•} ' + normal + "Nombre d'arcs : " + white + str(graph.nb_edge))
    pause(my_time_05)
    print(red + '\n{•} ' + normal + "Arcs : " + white, end='')

    i = 0
    for node in graph.list_node_object:
        for key, value in node.edges.items():
            if value != '*':
                i += 1
                pause(my_time_03)
                print('(' + node.name + graph.space(len(node.name)) + ')-[' +
                      str(node.duration) + graph.space(len(str(node.duration))) + ']->(' +
                      key + graph.space(len(key)) + ')  ', end='')
            if i == 3:
                print('\n           ', end='')
                i = 0


def pause(n):
    time.sleep(n)


my_time_03 = 0
my_time_05 = 0
my_time_1 = 0
my_time_2 = 0

normal = "\033[0m"
blue = "\033[0;94m"
red = "\033[0;91m"
yellow = "\033[0;93m"
green = "\033[0;32m"
white = "\033[0;97m"
bold = "\033[1m"
