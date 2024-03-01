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
    graph.calendrier_au_plus_tot()
    #Dans le cas où il n'y a pas de circuit dans le graphe alors on peut effectuer les calculs des questions 4-5-6 dans le if not
    if not graph.circuit:
        pass

