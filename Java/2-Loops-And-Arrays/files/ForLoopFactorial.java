import java.util.Scanner;

public class ForLoopFactorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        sc.close();

        int factorial = 1;

        if (number > 1) {
            for (int i = 2; i <= number; i++) {
                factorial *= i;
            }
        }

        System.out.println("Factorial of " + number + " is " + factorial);
    }
}
