public class Main {

    public static void main(String[] args) {
        // set the properties of the class using
        /*
         * Student student = new Student();
         * 
         * student.setId("std0012");
         * student.setFullName("John Adams");
         * student.setPassword("simple_password");
         */

        // Use the student constructor
        Student student = new Student(
                "std0012",
                "bunny",
                "John Adams");

        System.out.println("Full Name: " + student.getFullName());
        System.out.println("ID: " + student.getId());
        System.out.println("Password: " + student.getPassword());
        System.out.println();

        // student object with isClassRep
        Student studentRep = new Student(
                "std0013",
                "password",
                "Hannah Adams",
                true);

        System.out.println("Full Name: " + studentRep.getFullName());
        System.out.println("ID: " + studentRep.getId());
        System.out.println("Password: " + studentRep.getFullName());
        System.out.println(
                studentRep.getFullName()
                        + " is class president: "
                        + studentRep.isClassRep());
    }
}