public class Circle extends Shape {
    public Circle(String name, double radius) {
        super(name, radius);
    }

    /* area = PI * radius * radius or PI * radius squared */
    public double area() {
        return Math.round(Math.PI * Math.pow(this.getSide(), 2));
    }

    /*
     * A Circle's perimeter is the same as its circumference
     * perimeter = 2 * PI * radius
     */
    public double perimeter() {
        return Math.round(2 * Math.PI * this.getSide());
    }
}
