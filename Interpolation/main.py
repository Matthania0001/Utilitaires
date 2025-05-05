from donnees import Donnees
from graphes import gr_comp_ajout_points, courbe_interpolante, gr_comp_ajout_point_par_point
from operations import somme_Donnees
import numpy as np
import math as m
a = Donnees([(i, (i+1)**(-1)) for i in [-5,-3,-2,1,2,-4,-10]])
b = Donnees([(-1,5),(1.5,10)])
print(a)
#gr_comp_ajout_point_par_point(a, b)
gr_comp_ajout_points(a,b)
#courbe_interpolante(a)