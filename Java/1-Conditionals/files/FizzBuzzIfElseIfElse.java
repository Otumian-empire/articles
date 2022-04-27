import java.util.Scanner;

public class FizzBuzzIfElseIfElse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int userInput = scanner.nextInt();

        scanner.close();

        // check if it is divisible by 3 and 5
        if (userInput % 3 == 0) {
            if (userInput % 5 == 0) {
                System.out.println("FizzBuzz");
            } else {
                System.out.println("Fizz");
            }
        } else if (userInput % 5 == 0) {
            System.out.println("Buzz");
        } else {
            System.out.println(userInput);
        }

    }
}
