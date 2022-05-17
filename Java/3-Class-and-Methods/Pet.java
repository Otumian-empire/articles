public class Pet {
    public String name;
    public String favFood;
    public static int counter = 0;

    public void print() {
        System.out.println("Name: " + name);
        System.out.println("Favorite Food: " + favFood);
        counter++;
    }

    public static void cute() {
        System.out.println("Pet is cute");
    }
}