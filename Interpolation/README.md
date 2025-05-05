Objets:
  -Donnees(from Interpolation.donnees import Donnees)
  -Polynomes(from Interpolation.polynome import Polynome)

Methodes et attributs de l'objet Donnees:
  Soit t: Donnees
  -(Attribut) t.list_donnees retourne la liste de type list[(int|float, int|float)], les tuples est composés (abscisse,ordonnée)
  -(Methode) t.est_interpolable() retourne le Booleen True si t est un jeu de donnees est interpolable
Methode et attributs de l'objet Polynome:
  -(Attribut) t.monomes retourne la liste des monomes du polynome de type list[(int|float, int)], les tuples etant composés (coefficient,dégré)
  -(Méthode) t.reduction() retourne la liste réduite de t.monomes au sens ou on somme les monomes ayant un meme dégré
  -(Méthode) t.degre() retourne le dégré du polynome
  -(Méthode) t.ordre_croissant() retourne la liste ordonnée au sens croissant des dégré de t.monome
  -(Méthode) t.ordre_decroissant() retourne la liste ordonnée au sens décroissant des dégré de t.monome
  -(Méthode) t.exp_littéral(ordre = a) retourne une chaine de caractère étant l'expression littérale du polynome; expression decroissante si l'entier a = 1

Fonctions Générales:
  -poly_interpolant(d: Donnees, precision: int) retourne le polynome interpolant du jeu de données d si d est interpolable. Sinon elle retourne une erreur. La précision indique le nombre de chiffre après la virgule à prendre en considération
    * from Interpolation.interpolant import poly_interpolant
  -somme(des Polynome) retourne le polynome somme de tous les Polynome entré en parametre.
    * from Interpolation.operation import somme
  -opp(p: Polynome) retourne le polynome opposant du polynome p
    * from Interpolation.operation import opp
  -multi_par_scalaire(p: Polynome, c: int|float) retourne le polynome resultat de la multiplication de p par s
    *from Interpolation.operation import multi_par_scalaire
  -multiplication(p1: Polynome, p2: Polynome) retourne le polynome resultant du produit de p1 et p2
    *from Interpolation.operation import multiplication
  -exposant(p: Polynome, e: int) retourne p multiplié par lui meme e fois
    *from Interpolation.operation import exposant
  -evaluate(p: Polynome, v: int) retourne la valeur du polynome p en v
    *from Interpolation.operation evaluate
  -somme_Donnees(des Donnees) retourne un Donnees combinant tous les Donnees entrés en parametre.
    *from Interpolation.operation import msomme_Donnees
  -ligne_matrice_v(d: Donnees, position: int) retourne (position + 1)ème ligne de la matrice de Vendermonde associé au jeu de données d sous forme de liste
    *from INterpolation.vendermonde import ligne_matrice_v
  -matrice_v(d: Donnees) retourne la liste des ligne de la matrice de Vendermonde
    *from Interpolation.vendermonde import matrice_v
  -display_ligne(liste) affiche la liste sans les virgules et sans les crochets
    * from Interpolation.vendermonde import display_ligne
  -display(list[list[int|float]]) est une liste de listes qui donne une représentation matricielle
    *from Interpolation.vendermonde import display
  -courbe_interpolante(t: Donnees, precison: int) trace le graphe qui fait l'interpolation polynomiale du jeu de donnees d avec une précision spécifiée pour le polynome interpolant
    * from Interpolation.graphes import courbe_interpolante
  -gr_comp_ajout_points(t: Donnees, w: Donnees, precision: int) retourne deux courbes : celle du jeu de données de t et du jeu obtenu en faisant la somme de t et w
    * from Interpolation.graphes import gr_comp_ajout_points
  -gr_comp_ajout_point_par_point(t: Donnees,w: Donnees, precision = 100) retourn premierement une courbe interpolant t ensuite d'autres courbe interpolants les sommes de t et de chacun des elements de w
    * from Interpolation.graphes import gr_comp_ajout_point_par_point
