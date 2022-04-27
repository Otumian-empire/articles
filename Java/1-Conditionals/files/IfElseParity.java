import java.util.Scanner;

public class IfElseParity {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int userInput = scanner.nextInt();

        scanner.close();

        if (userInput % 2 == 0) {
            System.out.println(userInput + " is Even");
        } else {
            System.out.println(userInput + " is Odd");
        }
    }
}
