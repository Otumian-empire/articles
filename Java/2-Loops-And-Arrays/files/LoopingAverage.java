import java.util.Scanner;

public class LoopingAverage {
    public static void main(String[] args) {
        // int[] nums = new int[5];
        int numSum = 0;

        Scanner sc = new Scanner(System.in);

        // prompt user for the five scores
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter " + (i + 1) + "th score: ");
            // nums[i] = sc.nextInt();
            numSum += sc.nextInt();
        }

        sc.close();

        // int numSum = 0; // moved to the top

        // for (int i = 0; i < 5; i++) {
        // numSum += nums[i];
        // }

        // int numAvg = numSum / 5;

        System.out.println("Sum: " + numSum);
        System.out.println("Average: " + (numSum / 5));
    }
}
