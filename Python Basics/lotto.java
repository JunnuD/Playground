import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;

public class Lotto {

    public static void main(String[] args) {
        int[] lottonumerot = arvolottonumerot();
        int[] pelaajannumerot = kysyNumerot();
        tulostaLottonumerot(lottonumerot);
        tulostaPelaajannumerot(pelaajannumerot);
        int oikein = laskeOikein(pelaajannumerot, lottonumerot);
        System.out.println("Sait " + oikein + " oikein!");
    }

    public static int[] kysyNumerot() {
        Scanner lukija = new Scanner(System.in);
        int[] numerot = new int[7];
        System.out.println("Syötä seitsemän uniikkia numeroa välillä 1-40.");
        

        for (int i = 0; i < numerot.length; i++) {           
            System.out.print("Numero " + (i + 1) + ": ");
            numerot[i]=lukija.nextInt();
            
        }
        Arrays.sort(numerot);
        return numerot; 

    }
    
    public static int laskeOikein(int[] pelaajannumerot, int[] lottonumerot) {
        int oikein = 0;
        for (int i = 0; i < pelaajannumerot.length; i++) {
            if (sisaltaaNumeron(lottonumerot, pelaajannumerot[i])) {
                oikein++;
            }
        }
        return oikein;

    }
    
    public static int[] arvolottonumerot() {
        Random random = new Random();
        int[] numerot = new int[7];
        int arvottujenNumeroidenLukumaara = 0;
        
        while (arvottujenNumeroidenLukumaara < 7) {
            int arvottuNumero = random.nextInt(40) + 1;
            if (!sisaltaaNumeron(numerot, arvottuNumero)) {
                numerot[arvottujenNumeroidenLukumaara] = arvottuNumero;
                arvottujenNumeroidenLukumaara++;
            }
        }
        
        jarjestaNumerot(numerot);
        return numerot;
    }
    
    public static void jarjestaNumerot(int[] numerot) {
        for (int i = 0; i < numerot.length - 1; i++) {
            for (int b = i + 1; b < numerot.length; b++) {
                if (numerot[b] < numerot[i]) {
                    int temp = numerot[i];
                    numerot[i] = numerot[b];
                    numerot[b] = temp;
                }
            }
        }
    }
    
    public static boolean sisaltaaNumeron(int[] numerot, int etsittavaNumero) {
        for (int i = 0; i < numerot.length; i++) {
            if (numerot[i] == etsittavaNumero) {
                return true;
            }
        }
        return false;
    }
    
    public static void tulostaLottonumerot(int[] numerot) {
        System.out.print("Arvottu lottorivi: ");
        for (int i = 0; i < numerot.length; i++) {
            System.out.print(numerot[i] + " ");
        }
        System.out.println();
    }
    public static void tulostaPelaajannumerot(int[] numerot) {
        System.out.print("Pelaajan lottorivi: ");
        for (int i = 0; i < numerot.length; i++) {
            System.out.print(numerot[i] + " ");
        }
        System.out.println();
    }
}

