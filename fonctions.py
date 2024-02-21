
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


normal = "\033[0m"
blue = "\033[0;94m"
red = "\033[0;91m"
yellow = "\033[0;93m"
green = "\033[0;32m"
white = "\033[0;97m"
bold = "\033[1m"
