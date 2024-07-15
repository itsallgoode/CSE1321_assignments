import java.util.Scanner;

public class Lab13B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String name;
        do { 
            System.out.print("Enter a name for the book: ");
            name = sc.nextLine();
            if (name.isEmpty()) {
                System.out.println("Name cannot be empty.");

            }
        } while (name.isEmpty());

        int yearOfRelease;
        do { 
            System.out.print("Enter a year of release for the book: ");
            yearOfRelease = sc.nextInt();
            sc.nextLine();
            if (yearOfRelease < 1500 || yearOfRelease > 2024) {
                System.out.println("Year of release must be between 1500 and 2024.");
            }
        } while (yearOfRelease < 1500 || yearOfRelease > 2024);

        Book book = new Book(name, yearOfRelease);

        double price;

        do { 
            System.out.print("Enter a price for the book: ");
            price = sc.nextDouble();
            if (price <= 0) {
                System.out.println("Price must be a positive number.");
            }
        } while (price <= 0);

        book.setPrice(price);

        
        System.out.println("\n" + book.toString());
    }
}

class Book {
    private String name;
    private int yearOfRelease;
    private double price;

    public Book(String name, int yearOfRelease) {
        this.name = name;
        this.yearOfRelease = yearOfRelease;

    }

    public void setPrice(double price) {
        this.price = price;
    }

    public String toString() {
        return name + " (" + yearOfRelease + "): $" + price;
    }
}