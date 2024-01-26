import java.util.Random;
import java.util.Scanner;

public class KT2_7 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int parhaatYritykset = Integer.MAX_VALUE;
        int huonoimmatYritykset = Integer.MIN_VALUE;
        boolean peliJatkuu = true;

        do {

            int arvattuLuku = random.nextInt(100) + 1;

            System.out.println("Tervetuloa arvauspeliin! Arvaa luku väliltä 1-100.");

            int arvaus;
            int yritykset = 0;

            do {

                System.out.print("Syötä arvaus: ");
                arvaus = scanner.nextInt();
                yritykset++;


                if (arvaus == arvattuLuku) {
                    System.out.println("Onneksi olkoon! Arvasit oikein luvulla " + arvattuLuku + ". Käytit " + yritykset + " yritystä.");
                } else if (arvaus < arvattuLuku) {
                    System.out.println("Arvattu luku on suurempi. Yritä uudelleen.");
                } else {
                    System.out.println("Arvattu luku on pienempi. Yritä uudelleen.");
                }

            } while (arvaus != arvattuLuku);


            parhaatYritykset = Math.min(parhaatYritykset, yritykset);
            huonoimmatYritykset = Math.max(huonoimmatYritykset, yritykset);


            System.out.println("Arvauskierros päättyi. Arvauksia yhteensä: " + yritykset +
                    ". Paras tulos: " + parhaatYritykset + ". Huonoin tulos: " + huonoimmatYritykset);

            System.out.print("Valitse toiminto: 1) arvaa uusi luku 2) lopeta: ");
            int valinta = scanner.nextInt();

            if (valinta == 2) {
                peliJatkuu = false;
            }

        } while (peliJatkuu);

        scanner.close();
    }
}