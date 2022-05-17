public class StringMethods {
    public static void main(String[] args) {
        String str = "This is a string";

        // charAt - get the first element
        char firstCharacter = str.charAt(0);
        System.out.println("The first character is: " + firstCharacter);

        // concat
        String newStr = str.concat(", so Hello.");
        System.out.println(str); // this is the original string
        System.out.println(newStr); // this is the new string

        // concat is the same as str1 + str2
        String str1 = "Hello";
        String str2 = "World";
        String str3 = str1 + " " + str2;
        System.out.println(str3);

        // contains
        boolean hasWordString = str.contains("string");
        System.out.println("It is " + hasWordString + " that the string contains a word, \"string\".");

        // indexOf
        int indexOfIs = str.indexOf("m");
        System.out.println("The index of 'is' is, " + indexOfIs);

        // replace
        String replacedString = str.replace("string", "Double");
        System.out.println(replacedString);

        // split
        String[] splitString = str.split("");
        System.out.println(splitString.length);

        // substring
        String subString = str.substring(3, 10);
        System.out.println(subString);
    }
}
