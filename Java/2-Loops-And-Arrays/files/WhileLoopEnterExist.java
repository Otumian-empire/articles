import java.util.Scanner;

public class WhileLoopEnterExist {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String userInput = sc.next();

        while (!userInput.equals("exit")) {
            System.out.println("You entered " + userInput);
            userInput = sc.next();
        }

        sc.close();

        System.out.println("Program ended");
    }
}
