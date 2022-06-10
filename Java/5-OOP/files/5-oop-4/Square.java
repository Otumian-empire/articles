public class Square extends Shape {

    public Square(String name, double side) {
        super(name, side);
    }

    /* area = side * side or side squared */
    public double area() {
        return Math.pow(this.getSide(), 2);
    }

    /* perimeter = side + side + side + side or 4 * side */
    public double perimeter() {
        return 4 * this.getSide();
    }

}
