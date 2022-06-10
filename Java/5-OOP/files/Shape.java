public class Shape {
    private double length;
    private double breadth;

    // public Shape(double length, double breadth) {
    // length = length;
    // breadth = breadth;
    // }

    // public Shape(double l, double b) {
    // length = l;
    // breadth = b;
    // }

    public Shape(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    public double getBreadth() {
        return breadth;
    }

    public void setBreadth(double breadth) {
        this.breadth = breadth;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double area() {
        return this.length * this.breadth;
    }

    public double perimeter() {
        return 2 * (this.length + this.breadth);
    }

    // public void print() {
    // System.out.println("The shape has a length and a breadth of, "
    // + this.length + " and " + this.breadth + ".");
    // System.out.println("Shape has an Area of " + this.area()
    // + " squared units.");
    // System.out.println("Shape has a Perimeter of " + this.perimeter()
    // + " units.");
    // }
}
