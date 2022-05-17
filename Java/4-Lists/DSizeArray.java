package Java.Lists;
public class DSizeArray {

    public static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.println(i);
        }
    }

    public static int[] addElement(int[] arr, int el) {
        int[] newArr = new int[arr.length + 1];

        for (int i = 0; i < newArr.length; i++) {
            newArr[i] = arr[i];
        }

        newArr[newArr.length - 1] = el;

        return newArr;
    }

    public static void main(String[] args) {
        int[] arr = new int[3];

        arr[0] = 1;
        arr[1] = 3;
        arr[2] = 5;

        printArray(arr);
        System.out.println("\n");

        arr = addElement(arr, 8);
        printArray(arr);
    }
}