from operator import truediv

from interpolant import poly_interpolant
from polynome import Polynome
from donnees import Donnees

#Les opérations definies pour le type Polynome
def somme (*args: Polynome)-> Polynome:
    polynome: Polynome = Polynome([(0,0)])
    l = []
    for i in range (len(args)):
        for j in range(len(args[i].monomes)):
            l += [args[i].monomes[j]]
    polynome = Polynome(l)
    return polynome

def opp(t: Polynome) -> Polynome:
    polynome: Polynome = Polynome([(0,0)])
    l = []
    for i in range(len(t.monomes)):
        l += [(-t.monomes[i][0], t.monomes[i][1])]
    polynome = Polynome(l)
    return polynome

def multi_par_scalaire(t: Polynome, s: int|float):
    polynome: Polynome = Polynome([(0, 0)])
    l = []
    for i in range(len(t.monomes)):
        l += [(s * t.monomes[i][0], t.monomes[i][1])]
    polynome = Polynome(l)
    return polynome

def multiplication(t: Polynome, s: Polynome) -> Polynome:
    if len(s.monomes) == 1:
        polynome: Polynome = Polynome([(0, 0)])
        l = []
        for i in range(len(t.monomes)):
            l += [(s.monomes[0][0] * t.monomes[i][0], s.monomes[0][1] + t.monomes[i][1])]
        polynome = Polynome(l)
        return polynome
    else:
        polynome: Polynome = Polynome([(0, 0)])
        l = []
        for i in range(len(s.monomes)):
            l += multiplication(t, Polynome([s.monomes[i]])).monomes
        polynome = Polynome(l)
        return polynome

def exposant(t: Polynome, expo: int = None) -> Polynome:
    if expo == 0:
        return 1
    elif expo == 1:
        return t
    else:
       return multiplication(t,exposant(t,expo - 1))


def evaluate(t: Polynome, x: int | float):
    s = 0
    for i in range(len(t.monomes)):
        s += t.ordre_decroissant()[i][0] * (x**(t.ordre_decroissant()[i][1]))
    return s


# Operation definies pour les objets de type Donnees
def somme_Donnees(*args: Donnees):
    l: Donnees = Donnees([])
    for i in args:
            l.list_donnees += i.list_donnees
    return l


w = Donnees([(1,2),(2,3)])
z = Donnees([(3,4),(4,5)])
print(somme_Donnees(w,z).list_donnees)
'''b = [(2,3),(-4,7),(-1,4), (2,3), (4,3), (-8,0), (0,5)]
c = [(1,4)]
a = Polynome(b)
d = Polynome(b)
#print(a.ordre_croissant())
#print(a.exp_litteral(ordre = 1))
#print(a.exp_litteral(ordre = 0))
#print(multi_par_scalaire(opp(somme(a, d)), 3))

p1 = [(1,1),(1,0)]
p2 = [(1,1),(1,0),(2,3)]
P1 = Polynome(p1)
P2 = Polynome(p2)
#print(exposant(P1, 2).ordre_decroissant())
print(evaluate(P2, 3))
'''
