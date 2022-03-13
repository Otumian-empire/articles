import java.util.Scanner;

public class InputWithVariable {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // read in a line - fullName is separated by space
        System.out.print("Enter full name: ");
        String fullName = input.nextLine();

        // read in an integer value and assign it to age
        System.out.print("Enter age: ");
        int age = input.nextInt();

        // read in a character using the next()
        // because grade is of type char, it will take just the
        // first character from word with `.charAt(0)`
        System.out.print("Enter grade: ");
        char grade = input.next().charAt(0);

        // get boolean input, true/false
        System.out.print("Are you a programmer, enter: true|false: ");
        boolean isProgrammer = input.nextBoolean();

        // get a double just like int
        System.out.print("Enter weight: ");
        double weight = input.nextDouble();

        // close the scanner object
        input.close();

        // System.out.println() prints out a newline character after
        // its arguments
        System.out.println();
        System.out.println();

        System.out.println("My name is " + fullName);
        System.out.println("I am " + age + " years old");
        System.out.println("It is " + isProgrammer + " that I am a programmer");
        System.out.println("I want grade " + grade + " this semester");
        System.out.println("Now I weight, " + weight + "kg because of programming");
    }
}
