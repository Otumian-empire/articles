public class Main {
    public static void main(String[] args) {
        Pet bobby = new Pet();

        // We set the fields directly using the Pet instance
        bobby.name = "Bobby Peto";
        bobby.favFood = "Chicken and Salad cream";

        // call the print method
        bobby.print();

        // call the static method
        Pet.cute();

        // update the fields and call print
        bobby.name = "Bobby Pet";
        bobby.favFood = "Chicken, Broccoli and Salad cream";

        bobby.print();

        // call the static field
        System.out.println("the print method was called, " + Pet.counter + " times.");

    }
}
