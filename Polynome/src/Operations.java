public class Operations {
    //Fonction pour afficher les listes
    public static void Affichage_list(int[] l) {
        for (int j = 0; j < l.length; j++) {
            System.out.println(l[j]);
        }
    }
    //Fonction pour verifier si une entier se trouve dans une liste donnée
    public static boolean Find(int[] l, int d) {
        boolean temp = false;
        for (int i = 0; i < l.length; i++) {
            if (l[i] == d) {
                temp = true;
            }
        }
        ;
        return temp;
    };
    //Fonction qui renvoie la liste des différents degré du tableau de monomes
    public static int[] ListeDegres(Monome[] M) {
        int[] ll = new int[M.length];
        for (int j = 0; j < M.length; j++) {
            if (M[j].degre == 0) {
                ll[j] = -1;
            } else {
                if (Operations.Find(ll, M[j].degre) == false) {
                    ll[j] = M[j].degre;
                }
                ;
            }
            ;

        };
        int z = 0;
        for(int t = 0; t < ll.length; t++){
            if(ll[t] != 0){
                z += 1;
            };
        };
        int[] lll = new int[z];
        for(int t = 0; t < z; t++){
            lll[t] = ll[t];
        };
        for (int j = 0; j < lll.length; j++) {
            if (lll[j] == -1) {
                lll[j] = 0;
            }
            ;
        }
        return lll;
    };
    //La fonction reduit le liste de Monomes c'est a dire regroupe les monomes ayant le meme degré.
    public static Monome[] Reduction(Monome[] M) {
        //int[] liste_degres = new int[Operations.ListeDegres(M).length];
        Monome[] M_Reduit = new Monome[Operations.ListeDegres(M).length];
        for (int j = 0; j < Operations.ListeDegres(M).length; j++) {
            int d = Operations.ListeDegres(M)[j];
            int s = 0;
            for (int i = 0; i < M.length; i++) {
                if (M[i].degre == d) {
                    s += M[i].coef;
                }
            }
            M_Reduit[j] = new Monome(d, s);
        }
        return M_Reduit;
    };
    //Affichage du tableau de monomes sous forme d'expression littérale (Un tableau de Monomes ici est typiquement une polynome)
    public static void Affiche_Tab_Monome(Monome[] M) {
        for (int j = 0; j < M.length; j++) {
            if (M[j].degre == 0) {
                if (M[j].coef > 0) {
                    if (j == 0) {
                        System.out.print(M[j].coef);
                    } else {
                        System.out.print("+" + M[j].coef);
                    }
                } else {
                    if (M[j].coef < 0) {
                        System.out.print(M[j].coef);
                    } else {
                        continue;
                    }
                }

            } else {
                if (M[j].degre == 1) {
                    if (M[j].coef > 0) {
                        if (j == 0) {
                            System.out.print(M[j].coef + "x");
                        } else {
                            System.out.print("+" + M[j].coef + "x");
                        }
                    } else {
                        if (M[j].coef < 0) {
                            System.out.print(M[j].coef + "x");
                        } else {
                            continue;
                        }
                    }
                } else {
                    if (M[j].coef > 0) {
                        if (j == 0) {
                            System.out.print(M[j].coef + "x^(" + M[j].degre + ")");
                        } else {
                            System.out.print("+" + M[j].coef + "x^(" + M[j].degre + ")");
                        }
                    } else {
                        if (M[j].coef < 0) {
                            System.out.print(M[j].coef + "x^(" + M[j].degre + ")");
                        } else {
                            continue;
                        }
                    }
                }


            }
        }
    }
    //Range la liste de monomes dans l'ordre croissant de leur degré
    public static Monome[] Ordre_Croissant(Monome[] M) {
        Monome[] M1 = new Monome[Operations.Reduction(M).length];
        for (int j = 0; j < Operations.Reduction(M).length; j++) {
            M1[j] = new Monome(Operations.Reduction(M)[j].degre, Operations.Reduction(M)[j].coef);
        }
        for (int i = 0; i < M1.length - 1; i++) {
            for (int j = 0; j < M1.length - 1 - i; j++) {
                if (M1[j].degre > M1[j + 1].degre) {
                    Monome temp = new Monome(M1[j].degre, M1[j].coef);
                    M1[j] = new Monome(M1[j + 1].degre, M1[j + 1].coef);
                    M1[j + 1] = new Monome(temp.degre, temp.coef);
                }
            }
        }
        return M1;
    }
    //Range la liste de monomes dans l'ordre décroissant
    public static Monome[] Ordre_Decroissant(Monome[] M) {
        Monome[] M1 = new Monome[Operations.Ordre_Croissant(M).length];
        for (int j = 0; j < Operations.Reduction(M).length; j++) {
            M1[j] = new Monome(Operations.Ordre_Croissant(M)[Operations.Ordre_Croissant(M).length - j - 1].degre, Operations.Ordre_Croissant(M)[Operations.Reduction(M).length - j - 1].coef);
        }
        return M1;
    }

    public static Monome[] Somme_M_M(Monome M1, Monome M2) {
        int i = 0;
        if (M1.degre == M2.degre) {
            i = 1;
        } else {
            i = 2;
        }
        Monome[] l = new Monome[i];
        Monome M3 = new Monome(0, 0);
        if (M1.degre == M2.degre) {
            M3.degre = M1.degre;
            M3.coef = M1.coef + M2.coef;
            l[0] = M3;
        } else {
            l[0] = M1;
            l[1] = M2;
        }
        return l;
    }

    ;

    public static Monome[] Somme_M_P(Monome M, Polynome P) {
        boolean temp = false;
        int z = 0;
        for (int i = 0; i < Operations.Reduction(P.M).length; i++) {
            if (P.M[i].degre == M.degre) {
                temp = true;
            }
        }
        if (temp == true){
            z = Operations.Reduction(P.M).length;
        }
        else{
            z = Operations.Reduction(P.M).length + 1;
        }
        Monome[] M1 = new Monome[z];
        if (temp == true) {
            for (int i = 0; i < Operations.Reduction(P.M).length; i++) {
                if (P.M[i].degre == M.degre) {
                    M1[i] = new Monome(M.degre, M.coef + Operations.Reduction(P.M)[i].coef);
                }
                else{
                    M1[i] = new Monome(Operations.Reduction(P.M)[i].degre, Operations.Reduction(P.M)[i].coef);
                }
            }
        }
        else{
            for (int i = 0; i < Operations.Reduction(P.M).length; i++){
                M1[i] = new Monome(Operations.Reduction(P.M)[i].degre, Operations.Reduction(P.M)[i].coef);
            }
            M1[Operations.Reduction(P.M).length] = new Monome(M.degre, M.coef);
        }
        return M1;
    }
    public static Monome[] Somme_P_P(Polynome P1, Polynome P2){
        int n = P1.M.length + P2.M.length;
        Monome[] M1 = new Monome[n];
        for(int i = 0; i < P1.M.length; i++){
            M1[i] = new Monome(P1.M[i].degre, P1.M[i].coef);
        };
        for(int j = P1.M.length; j < n; j++){
            M1[j] = new Monome(P2.M[j].degre, P2.M[j].coef);
        }
        return Operations.Reduction(M1);
    }
    public static Monome Produit_M_M(Monome M1, Monome M2){
        Monome M = new Monome(M1.degre + M2.degre, M1.coef * M2.coef);
        return M;
    };
    public static Monome[] Produit_M_P(Monome M, Polynome P){
        Monome[] M1 = new Monome[P.M.length];
        for(int i = 0; i < P.M.length; i++){
            M1[i] = new Monome(Operations.Produit_M_M(M, P.M[i]).degre, Operations.Produit_M_M(M, P.M[i]).coef);
        }
        return M1;
    }
    //Calcul du produit de deux Polynomes
    public static Monome[] Produit_P_P(Polynome P1, Polynome P2){
        int n = P1.M.length * P2.M.length;
        Monome[][] M = new Monome[P1.M.length][P2.M.length];
        for(int i = 0; i < P1.M.length; i++){
            for(int j = 0; j < P2.M.length; j++){
                M[i][j] = new Monome(Operations.Produit_M_M(P1.M[i], P2.M[j]).degre, Operations.Produit_M_M(P1.M[i], P2.M[j]).coef);
            }
        }
        Monome[] M1 = new Monome[n];
        for(int i = 0; i < P1.M.length; i++){
            for(int j = 0; j < P2.M.length; j++){
                M1[i * P2.M.length + j] = new Monome(M[i][j].degre, M[i][j].coef);
            };
        };
        return Operations.Reduction(M1);
    }
}
