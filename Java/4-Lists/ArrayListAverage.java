import java.util.ArrayList;

public class ArrayListAverage {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>(5);

        nums.add(3);
        nums.add(2);
        nums.add(1);
        nums.add(5);
        nums.add(4);

        int numSum = nums.get(0) + nums.get(1) + nums.get(2) + nums.get(3) + nums.get(4);

        double numAvg = (double)numSum / nums.size();

        System.out.println("Sum: " + numSum);
        System.out.println("Average: " + numAvg);

        System.out.println("\n\nadd new element and find the sum and average");

        nums.add(6);
        numSum += nums.get(5);

        numAvg = (double)numSum / nums.size();

        System.out.println("New Sum: " + numSum);
        System.out.println("New  Average: " + numAvg);
    }
}
