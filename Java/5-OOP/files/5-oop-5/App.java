// App.java
public class App {

    private static void printResponse(User.Response res) {
        System.out.println("Registration status: " + res.getSuccess());
        System.out.println("Message: " + res.getMessage());

        if (res.getSuccess()) {
            System.out.println("User");
            System.out.println("Id: " + User.getId());
            System.out.println("Full name: " + res.getUser().getFullName());
            System.out.println("Email: " + res.getUser().getEmail());
        }
    }

    public static void main(String[] args) {

        User john = new User("John Doe", "johndoe@email.com", "password");

        User.Response res = john.signup();

        printResponse(res);

    }

}
