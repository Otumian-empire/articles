public class Student extends Human {

    private boolean isClassRep;

    public Student() {
    }

    public Student(String id, String password, String fullName) {
        super(id, password, fullName);
    }

    public Student(String id, String password, String fullName, boolean isClassRep) {
        super(id, password, fullName);
        this.isClassRep = isClassRep; // not added to super
        // this.setClassRep(isClassRep); // same as the above
    }

    public boolean isClassRep() {
        return this.isClassRep;
    }

    public void setClassRep(boolean isClassRep) {
        this.isClassRep = isClassRep;
    }

}
