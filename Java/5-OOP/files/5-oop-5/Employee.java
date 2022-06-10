// Employee.java
public class Employee {

    private String name;
    private double salary = 200;

    public Employee(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public void calculateRate() {
        this.salary += this.salary * 0.5;
    }

    public void print() {
        System.out.println("Name: " + name);
        System.out.println("Salary: " + salary);
        System.out.println();
    }

}
