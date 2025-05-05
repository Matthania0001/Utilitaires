class Donnees ():
    def __init__(self, a: list[tuple[int | float, int | float]]):
        self.list_donnees = a

    def __str__(self):
        for i in range(len(self.list_donnees)):
            print(f"f({self.list_donnees[i][0]}) = {self.list_donnees[i][1]}")
        return ""

    def est_interpolable(self):
        t = []
        for i in range(len(self.list_donnees)):
            if self.list_donnees[i][0] not in t:
                t += [self.list_donnees[i][0]]
        return len(t) == len(self.list_donnees)


'''a = Donnees([(1,2),(2,3),(6,3)])
a = Donnees([(i, np.log(i)) for i in range(1,11)] + [(11,2)])

b = Donnees([(11,2)])
print(a.est_interpolable())
'''