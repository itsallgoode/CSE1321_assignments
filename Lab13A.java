import java.util.Arrays;
import java.util.Scanner;

public class Lab13A {

    public static int min(int[] arr) {
        return Arrays.stream(arr).min().getAsInt();
    }

    public static int max(int[] arr) {
        return Arrays.stream(arr).max().getAsInt();
    }

    public static double avg(int[] arr) {
        return Arrays.stream(arr).average().getAsDouble();
    }

    public static void main(String[] args) {
        int size;
        Scanner sc = new Scanner(System.in);

        do {
            System.out.print("How many numbers would you like to enter? ");
            size = sc.nextInt();

            if (size <= 0) {
                System.out.println("You must enter a value that is greater than 0.");
            }

        } while (size <= 0);

        int[] arr = new int[size];

        for (int i = 0; i < size; i++) {
            System.out.print("Enter number " + i + ": ");
            arr[i] = sc.nextInt();
        }

        int choice;
        do {
            System.out.println("1 - Find the smallest of the numbers entered");
            System.out.println("2 - Find the largest of the numbers entered");
            System.out.println("3 - Find the average of the numbers entered");
            System.out.println("4 - Quit");
            System.out.print("Enter your option: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("The smallest of the numbers you entered is " + min(arr));
                    break;
                case 2:
                    System.out.println("The largest of the numbers you entered is " + max(arr));
                    break;
                case 3:
                    System.out.println("The average of the numbers you entered is " + avg(arr));
                    break;
                case 4:
                    System.out.println("Shutting off...");
                    break;
                default:
                    System.out.println("That is not a valid option!");
                    break;
            }

        } while (choice != 4);
    }

}
