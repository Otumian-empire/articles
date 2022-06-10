public class Square implements IShape {
    private double side;

    public Square(double side) {
        this.side = side;
    }

    public double area() {
        return Math.pow(this.side, 2);
    }

    public double perimeter() {
        return 4 * this.side;
    }

    public void print() {
        System.out.print("This square has an area of " + this.area());
        System.out.println(" and a perimeter of " + this.perimeter());
    }
}
