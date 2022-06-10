public class Sum {

    public int add() {
        return 10 + 2;
    }

    public int add(int a) {
        return a + 1;
    }

    public int add(int a, int b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public double add(double a, double b, double c) {
        return a + b + c;
    }

    public String add(String a, String b) {
        return a + " " + b;
    }

    public void add(String a) {
        System.out.println("We are just adding: " + a);
    }

}