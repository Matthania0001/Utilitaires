from donnees import Donnees
from vendermonde import matrice_v
from polynome import Polynome
import numpy as np
def poly_interpolant(d: Donnees , precision: int = 5):
    polynome: Polynome = Polynome([(0, 0)])
    n = len(d.list_donnees)
    vender = np.array(matrice_v(d), dtype= np.float64)
    b = np.array([d.list_donnees[i][1] for i in range(len(d.list_donnees))], dtype= np.float64)
    X = np.linalg.solve(vender, b)
    l = list(np.round(X, precision))
    return Polynome([(l[i], i) for i in range(n)])

t = Donnees([(1,2),(2,3),(3,4),(4,5),(5,1)])

print(poly_interpolant(t))