public class Human {

    private String id;
    private String password;
    private String fullName;

    public Human() {
    }

    public Human(
            String id,
            String password,
            String fullName) {
        this.id = id;
        this.password = password;
        this.fullName = fullName;
    }

    public String getId() {
        return this.id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPassword() {
        return this.password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getFullName() {
        return this.fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }
}