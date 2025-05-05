import java.util.Scanner;

public class Polynome {
    Monome[] M;
    Scanner Sc = new Scanner(System.in);
    public Polynome(){
        for(int i = 0; i < 100; i++) {
            System.out.println("Saisir le degré: ");
            M[i].degre = Sc.nextInt();
            System.out.println("Saisir le coefficient: ");
            M[i].coef = Sc.nextInt();
        };
    };
    public Polynome(Monome[] M){
        this.M = M;
    }
    public static Polynome Somme(Polynome P1, Polynome P2){
        return null;
    }

}