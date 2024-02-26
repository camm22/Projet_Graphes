# beginning of the program

# import of menu function
from fonction_menu import *

print(white + "\n###################################################################\n"
              "##############{-Projet : Ordonnancement de graphes-}###############\n"
              "###################################################################")

print(red + "\n*Vous pouvez quitter le programme ou revenir en arrière à tout moment en entrant \"q\" lors des inputs*")

choices_list = ['q']

for i in range(1, 5+1):
    choices_list.append(str(i))

# Possible value for secure entry


while 1:
    # infinite while loop which runs the program until it stops (this is the main loop)

    print(blue + "\n[-]Le programme possède actuellement", len(choices_list) - 1,
          "graphes. Lequel voulez-vous exécuter ?" + normal)

    # choice of graph to test

    choice = input(" ---> :")
    while choice not in choices_list:
        print(red + "\n[!]Ce graphe n'existe pas. Veuillez réessayer." + normal)
        choice = input(" ---> :")

    # secure entry of the choice of graph to test

    if choice == 'q':
        print(white + "\n###################################################################\n"
                      "################{-Mise hors tension du programme-}#################\n"
                      "###################################################################" + normal)
        break

    # the program turns off if the user enters "q"

    path = "documents\\graphes_de_test\\graphe" + choice + ".txt"

    # creation of the path of the graph to execute

    menu(True, path, choice)
    

    # calling the menu function
