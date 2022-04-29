import java.util.Scanner;

public class DoWhileLoopFactorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        sc.close();

        int factorial = 1;

        if (number > 1) {
            int i = 2;

            do {
                factorial *= i;
                i++;
            } while (i <= number);
        }

        System.out.println("Factorial of " + number + " is " + factorial);
    }
}
