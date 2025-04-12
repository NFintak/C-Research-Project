package Demo;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        fibSequenceForLoop(10);
        fibSequenceWhileLoop(10);
        stringUtils();
    }

    static public void fibSequenceForLoop(int x) {
        System.out.print("Fibonacci Sequence:");
        int sum = 1;
        int firstNum = 0;
        int nextNum = 1;
        for (int i = 0; i < x; i++) {
            System.out.print(" " + sum);
            sum = firstNum + nextNum;
            firstNum = nextNum;
            nextNum = sum;
        }
        System.out.println("\n");
    }

    static public void fibSequenceWhileLoop(int x) {
        int sum = 1;
        int firstNum = 0;
        int nextNum = 1;
        int i = 0;
        while (i < x) {
            System.out.println(sum);
            sum = firstNum + nextNum;
            firstNum = nextNum;
            nextNum = sum;
            i++;
        }
    }

    static public void stringUtils() {
        String[] languages = {"C#", "Java", "Python", "JavaScript"};
        String[] langsUpper = new String[4];
        String[] langsLower = new String[languages.length];
        for (int i = 0; i < langsUpper.length; i++) {
            langsUpper[i] = languages[i].toUpperCase();
        }
        for (int i = 0; i < langsLower.length; i++) {
            langsLower[i] = languages[i].toLowerCase();
        }
        for (int i = 0; i < languages.length; i++) {
            System.out.print(languages[i] + " ");
            System.out.print(langsUpper[i] + " ");
            System.out.print(langsLower[i] + "\n");
        }

    }
}