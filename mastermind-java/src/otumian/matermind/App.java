package src.otumian.matermind;

import java.util.ArrayList;
import java.util.Objects;
import java.util.Scanner;

// Use the random method of the Math class to generate random numbers between 0 and 9

public class App {
    public App() {

        // The number of times to play must be even between 2 and 12 rounds
        int rounds = 2;
        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                System.out.print("Enter number of rounds (Even in [2, 12]): ");
                rounds = Integer.parseInt(scanner.nextLine());

                if (rounds >= 2 && rounds <= 12 && rounds % 2 == 0) {
                    break;
                }

            } catch (Exception e) {
                System.out.println("Round must be an even number from 2 to 12 includes");
            }
        }

        // should there be duplicates
        int duplicates_allowed = 0;

        try {
            // Scanner scanner = new Scanner(System.in);
            System.out.print("Duplicates allowed? (1/0) ");
            duplicates_allowed = Integer.parseInt(scanner.nextLine());

            // scanner.close();

        } catch (Exception ignored) {
        }

        // The number of codes we will be dealing with will four
        final int NUMBER_CODE = 4;

        // The code maker
        ArrayList<Integer> code_maker = new ArrayList<>();
        int counter = 0;

        while (counter < NUMBER_CODE) {
            int code = genRand();

            if (duplicates_allowed == 1) {
                code_maker.add(code);
                counter += 1;
            } else {
                if (!code_maker.contains(code)) {
                    code_maker.add(code);
                    counter += 1;
                }

            }
        }

        // hint
        ArrayList<Integer> hints = new ArrayList<>();
        hints.add(2);
        hints.add(2);
        hints.add(2);
        hints.add(2);

        // code breaker guesses the code by the code maker
        while (rounds > 0) {

            // enter guess with spaces
            // Scanner scanner = new Scanner(System.in);
            System.out.print("Enter codes space separated: ");

            String[] inputs = scanner.nextLine().split(" ");

            ArrayList<Integer> code_breaker = new ArrayList<>();

            for (int i = 0; i < NUMBER_CODE; i++) {
                code_breaker.add(i, Integer.parseInt(inputs[i]));
            }

            // compare the code_breaker to the code maker
            for (int i = 0; i < NUMBER_CODE; i++) {
                if (code_breaker.get(i) > code_maker.get(i)) {
                    hints.set(i, 1);
                } else if (Objects.equals(code_breaker.get(i), code_maker.get(i))) {
                    hints.set(i, 0);
                } else {
                    hints.set(i, -1);
                }
            }

            // because of the values that we used to hint the user
            // we have to find some dicey way to break the program
            // when the user guess the code
            if (countZero(hints) == 4) {
                break;
            }

            System.out.println("# " + hints.toString());

            rounds -= 1;
        }

        // declaring the result of the game
        if (rounds > 0) {
            System.out.println("You won the rounds");
        } else {
            System.out.println("You lost bitterly to a computer");
        }

        System.out.println(code_maker.toString());
        scanner.close();

    }

    public static void main(String[] args) {

        new App();

    }

    // generate a random number
    public int genRand() {
        return (int) (10.0 * Math.random());
    }

    int countZero(ArrayList<Integer> arr) {
        int count = 0;

        for (int i : arr) {
            if (i == 0) {
                count++;
            }
        }

        return count;
    }
}
