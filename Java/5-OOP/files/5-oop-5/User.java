// User.java
public class User {
    private static int id = 0;
    private String fullName;
    private String email;
    private String password;

    public User(String fullName, String email, String password) {
        this.fullName = fullName;
        this.email = email;
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public String getFullName() {
        return fullName;
    }

    public static int getId() {
        return id;
    }

    public User.Response signup() {
        User.Validation validation = new User.Validation();

        boolean isValidEmail = validation.email(this.email);
        boolean isValidFullName = validation.name(this.fullName);
        boolean isValidPassword = validation.password(this.password);

        User.Response response = new User.Response();

        if (isValidEmail && isValidFullName && isValidPassword) {
            User.id += 1;
            response = new User.Response(true, "Signup successful", this);
        }

        return response.getResponse();

    }

    // this is a nested class used for validating the user properties
    private class Validation {

        private boolean name(String name) {
            return !name.isEmpty() && name.trim().length() > 3;
        }

        private boolean email(String email) {
            return !email.isEmpty() && email.trim().contains("@");
        }

        private boolean password(String password) {
            return !password.isEmpty() && password.trim().length() > 2;
        }
    }

    // this is a nested class used for returning response after signup
    class Response {
        private boolean success = false;
        private String message = "Signup unsuccessful";
        private User user = null;

        // for the default values above so that when the process fails
        // I won't have to pass the success status and message
        private Response() {
        }

        private Response(boolean success, String message, User user) {
            this.success = success;
            this.message = message;
            this.user = user;
        }

        public boolean getSuccess() {
            return success;
        }

        public String getMessage() {
            return message;
        }

        public User getUser() {
            return user;
        }

        public Response getResponse() {
            return this;
        }
    }
}
