import java.util.Scanner;

// MathClass.java

public class MathClass {
    public static void main(String[] args) {
        System.out.println("The max of 3 and 5 is: " + Math.max(3, 5));
        System.out.println();

        double dValue = 1.4365;
        System.out.println("Ceil(" + dValue + "): " + Math.ceil(dValue));
        System.out.println("Floor(" + dValue + "): " + Math.floor(dValue));
        System.out.println();

        // generate 5 random numbers
        for (int i = 0; i < 5; i++) {
            System.out.println(i + 1 + "th number: " + Math.random());
        }
        System.out.println();

        // Generate random numbers between x and y, where x < y
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Min: ");
        int minValue = sc.nextInt();

        System.out.print("Enter Min: ");
        int maxValue = sc.nextInt();

        sc.close();

        for (int i = 0; i < 100; i++) {
            // cast the double in to int `(int) SOME_DOUBLE_VALUE`
            int randValue = (int) Math.floor(Math.random() * (maxValue - minValue + 1) + minValue);

            System.out.println(randValue);
        }
    }
}