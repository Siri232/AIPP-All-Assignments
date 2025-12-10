import java.util.Scanner;

public class Main {

    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println("The number is positive");
        } else if (num < 0) {
            System.out.println("The number is negative");
        } else {
            System.out.println("The number is zero");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("--- Java Function Calls ---");
        System.out.print("Enter a number to check: ");

        if (sc.hasNextLine()) {
            String input = sc.nextLine();

            try {
                int num = Integer.parseInt(input.trim());
                checkNumber(num);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter an integer.");
            }
        } else {
            System.out.println("No input provided.");
        }
        sc.close();
    }
}