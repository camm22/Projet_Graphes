from graphe import *


def menu(power, path, graph_choice):

    print(red + bold + "\n--------[Création du graphe n°" + graph_choice + "]--------\n" + normal)

    graph = Graph()
    graph.readGraphFromFile(path)

    pause(my_time_1)
    print(yellow + "\n[*]Voici la matrice de valeurs du graphe n°" + graph_choice + " :\n" + normal)
    pause(my_time_2)

    graph.displayGraph()
    graph.areEdgesPositive(True)

    #graph.showGraph()

    graph.detecter_circuit()