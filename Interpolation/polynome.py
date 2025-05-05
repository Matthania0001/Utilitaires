class Polynome():
    def __init__(self, a: list[tuple[int | float, int]]):
        self.monomes = a
    def reduction(self):
        l: list[tuple[int | float, int | float]] = []
        #liste des coefficient w
        w: list[int | float] = []
        # t est la liste des degrées des monomes
        t: list[int] = []
        for i in range(len(self.monomes)):
            if self.monomes[i][1] not in t:
                t += [self.monomes[i][1]]
        for j in range(len(t)):
            s = 0
            for i in range(len(self.monomes)):
                if self.monomes[i][1] == t[j]:
                    s += self.monomes[i][0]
            w += [s]
        l = [(w[j], t[j]) for j in range(len(t))]
        return l

    def degre(self):
        l_degre: list[int | float] = [l[1] for l in self.monomes]
        return max(l_degre)

#les fonctions ordre_croissant et ordre_decroissant utilise directement la fonction reduction pour reduire les monome de meme exposants
    def ordre_croissant(self):
        n = len(self.reduction())
        l = self.reduction()
        for i in range(n):
            for j in range(n-i-1):
                if l[j][1] >= l[j+1][1]:
                    l[j], l[j+1] = l[j+1], l[j]
        return l
    def ordre_decroissant(self):
        l = self.ordre_croissant()
        return l[::-1]
    def exp_litteral(self, ordre = None):
        s = ""
        if len(self.monomes) == 1:
            if self.monomes[0][0] == 0:
                return 0
            elif self.monomes[0][0] == 1:
                if self.monomes[0][1] == 0:
                    return str(self.monomes[0][0])
                elif self.monomes[0][1] == 1:
                    return f"x"
                else:
                    return f"x^({self.monomes[0][1]})"
            else:
                if self.monomes[0][1] == 0:
                    return str(self.monomes[0][0])
                elif self.monomes[0][1] == 1:
                    return f"{self.monomes[0][0]}x"
                else:
                    return f"{self.monomes[0][0]}x^({self.monomes[0][1]})"
        if len(self.ordre_decroissant()) > 1:
            if ordre == 1:
                l = self.ordre_decroissant()
                for i in range(0, len(l)-1):
                    if l[i][0]:
                        if abs(l[i][0]) != 1:
                            if l[i][0] > 0:
                                s += f"+ {abs(l[i][0])}x^({l[i][1]}) "
                            elif l[i][0] < 0:
                                s += f"- {abs(l[i][0])}x^({l[i][1]}) "
                        else:
                            if l[i][0] > 0:
                                s += f"+ x^({l[i][1]}) "
                            elif l[i][0] < 0:
                                s += f"- x^({l[i][1]}) "
                if l[-1][0] != 0:
                    if l[-1][1] == 0:
                        if l[-1][0] > 0:
                            s += f"+ {abs(l[-1][0])}"
                        elif l[-1][0] < 0:
                            s += f"- {abs(l[-1][0])}"
                    else:
                        if l[1][0] > 0:
                            s += f"+ {abs(l[-1][0])}x^({l[-1][1]})"
                        elif l[1][0] < 0:
                            s += f"- {abs(l[-1][0])}x^({l[-1][1]})"
            else:
                l = self.ordre_croissant()
                if l[0][0] != 0:
                    if l[0][1] == 0:
                        s += f"{l[0][0]} "
                    else:
                        s += f"{l[0][0]}x^({l[0][1]}) "
                for i in range(1, len(l)):
                    if l[i][0]:
                        if abs(l[i][0]) != 1:
                            if l[i][0] > 0:
                                s += f"+ {abs(l[i][0])}x^({l[i][1]}) "
                            elif l[i][0] < 0:
                                s += f"- {abs(l[i][0])}x^({l[i][1]}) "
                        else:
                            if l[i][0] >0:
                                s += f"+ x^({l[i][1]}) "
                            elif l[i][0] < 0:
                                s += f"- x^({l[i][1]}) "
        return s

    def __str__(self):
        return self.exp_litteral(ordre = 1)















