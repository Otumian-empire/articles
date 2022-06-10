public abstract class Shape {
    private String name;
    private double side;

    public Shape(String name, double side) {
        this.name = name;
        this.side = side;
    }

    public double getSide() {
        return this.side;
    }

    // abstract methods
    public abstract double area();

    public abstract double perimeter();

    // default methods
    public void print() {
        System.out.print("This " + this.name + " has an Area of "
                + this.area() + " squared units");

        System.out.println(" and a Perimeter of "
                + this.perimeter() + " units.");
    }
}
