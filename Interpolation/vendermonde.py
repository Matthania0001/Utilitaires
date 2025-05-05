from donnees import Donnees
import numpy as np
def ligne_matrice_v(d: Donnees, position: int) -> list[int|float]:
    if d.est_interpolable():
        l = d.list_donnees
        return [[l[position][0]**j for j in range(len(l))]]
    else:
        return "Erreur: Jeu de données non-interpolable"
def matrice_v(d: Donnees) -> list[list[int|float]]:
    if d.est_interpolable():
        l = d.list_donnees
        t = []
        for i in range(len(l)):
            t += ligne_matrice_v(d, i)
        return t
    else:
        return "Erreur: les points ne sont pas d'abscisses deux à deux distincts"
def display_ligne(m: list[list], position: int) -> str:
    assert position <= len(m) - 1
    for i in range(len(m)):
            size = max([len(str(m[i][t])) for t in range(len(m[0]))])
            if i != len(m) -1:
                print(str(m[position][i]).rjust(size, " "), end="  ")
            else:
                print(str(m[position][i]).rjust(size, " "), end="  " + "\n")
    return ""
def display(m: list[list]) -> str:
    for i in range(len(m)):
        display_ligne(m, i)
    return ""

#a = Donnees([(0,1),(1,2)])
#print(matrice_v(a))