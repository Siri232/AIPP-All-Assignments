import java.util.*;

class Car {
    String brand, model;
    int year;

    Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read input (CodeChef-compatible)
        String brand = sc.nextLine().trim();
        String model = sc.nextLine().trim();
        int year = Integer.parseInt(sc.nextLine().trim());

        // Create object
        Car car = new Car(brand, model, year);

        // Display details
        car.displayDetails();

        sc.close();
    }
}
