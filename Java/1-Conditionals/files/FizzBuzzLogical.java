import java.util.Scanner;

public class FizzBuzzLogical {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int userInput = scanner.nextInt();

        scanner.close();

        if (userInput % 3 == 0 && userInput % 5 == 0) {
            System.out.println("FizzBuzz");
        } else if (userInput % 3 == 0) {
            System.out.println("Fizz");
        } else if (userInput % 5 == 0) {
            System.out.println("Buzz");
        } else {
            System.out.println(userInput);
        }

    }
}
