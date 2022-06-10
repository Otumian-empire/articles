// DayEnum.java

public class DayEnum {
    public enum Day {
        MONDAY,
        TUESDAY,
        WEDNESDAY,
        THURSDAY,
        FRIDAY,
        SATURDAY,
        SUNDAY;

        public void salutation() {
            System.out.println("Hey, today is " + this.name().toLowerCase());
        }
    }

    public static void printDay(Day day) {
        System.out.println("Today is, " + day.name().toLowerCase());
    }

    public static void printDayToString(Day day) {
        System.out.println("Today is, " + day.toString());
    }

    public static void printOrdinal(Day day) {
        System.out.println("The ordinal for " + day.name() + " is " + day.ordinal());
    }

    public static void main(String[] args) {
        Day day = Day.THURSDAY;

        printDay(day);

        printDayToString(day);

        printOrdinal(day);

        System.out.println(Day.valueOf("MONDAY"));

        System.out.println(day.compareTo(Day.MONDAY));

        System.out.println(day.equals(Day.FRIDAY));

        for (Day d : Day.values()) {
            System.out.println(d);
        }

        day.salutation();
    }
}