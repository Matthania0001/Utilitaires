import java.util.Scanner;

public class Monome {
    int degre;
    int coef;
    public Monome(int degre, int coef){
        this.degre = degre;
        this.coef = coef;
    };
    public Monome(){
        Scanner Sc = new Scanner(System.in);
        System.out.println("Saisir le degré: ");
        this.degre = Sc.nextInt();
        System.out.println("Saisir le coefficient: ");
        this.coef = Sc.nextInt();
    };
    public static int Search(Monome[] Tab,Monome M){
        int temp = -1;
        for(int i=0; i<Tab.length; i++){
            if (Tab[i] == M) {
                temp = i;
            };
        };
        return temp;
    };
    public static Monome Somme(Monome M1, Monome M2){
        int d1 = M1.degre;
        int d2 = M2.degre;
        int c1 = M1.coef;
        int c2 = M2.coef;
        if (d1 == d2){
            Monome M3 = new Monome();
            M3.degre = d1;
            M3.coef = c1 + c2;
            return M3;
        }
        else{
            System.out.println("Erreur: Les monomes doivent avoir le meme degré.");
            return null;
        }
    };
    public static Monome Multiplication(Monome M1, Monome M2){
        int d1 = M1.degre;
        int d2 = M2.degre;
        int c1 = M1.coef;
        int c2 = M2.coef;
        Monome M3 = new Monome();
        M3.degre = d1 + d2;
        M3.coef = d1 * d2;
        return M3;
    };
    public static Monome[] meme_degre(Monome [] M, int d){
        Monome[] M1 = new Monome[M.length];
        int i = 0;
        for(int j = 0 ; j < M.length;j++){
            if(M[j].degre == d){
                M1[i] = M[j];
                i += 1;
            }
        };
        return M1;
    };
    public static String toString(Monome M){
        return M.coef + "x^(" + M.degre + ")";
    };
    public static void Affichage(Monome[] M){
        for(int i = 0; i < M.length; i++) {
            System.out.println(toString(M[i]));
        };
    }


}
