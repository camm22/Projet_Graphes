from graphe import *


def menu(power, path, graph_choice):

    print(yellow + "\n[*]Voici la matrice de valeurs du graphe n°" + graph_choice + " :\n" + normal)

    graph = Graph()
    graph.readGraphFromFile(path)
    graph.displayGraph()

    graph.areEdgesPositive(True)


