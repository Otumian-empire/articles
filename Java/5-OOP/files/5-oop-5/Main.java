// Main.java
public class Main {
    enum Day {
        Monday, Tuesday, Wednesday
    }

    public static void main(String[] args) {
        System.out.println(Day.Monday.ordinal());
    }

    /*
     * public static void main(String[] args) {
     * // this is peter parker and he is not a rated employee
     * Employee peter = new Employee("Peter Parker");
     * peter.print();
     * 
     * // this is harry potter and he is also not a rated employee
     * Employee harry = new Employee("Harry Potter");
     * harry.print();
     * 
     * // the employer smiles on harry potter and harry becomes rated
     * // management now processes harry's salary
     * harry.calculateRate();
     * System.out.println();
     * 
     * // this is rated harry potter
     * harry.print();
     * 
     * // this is john doe and is not a rated employee
     * Employee john = new Employee("John Doe") {
     * 
     * @Override
     * public void calculateRate() {
     * double johnSalary = this.getSalary();
     * 
     * johnSalary += johnSalary * 0.15;
     * this.setSalary(johnSalary);
     * }
     * };
     * 
     * // the employer smiles on john so john becomes rated
     * // management now processes john's salary
     * john.calculateRate();
     * System.out.println();
     * 
     * // this is rated john doe
     * john.print();
     * 
     * }
     */
}