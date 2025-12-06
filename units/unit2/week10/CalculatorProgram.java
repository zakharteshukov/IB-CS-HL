import java.util.Scanner;

public class CalculatorProgram {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        
        do {
            System.out.println("\n=== Calculator Program Menu ===");
            System.out.println("1. Sum, Product, and Difference of Two Numbers");
            System.out.println("2. Student Marks Calculator");
            System.out.println("3. Square and Cube of a Number");
            System.out.println("4. Division of Two Floating-Point Numbers");
            System.out.println("5. Simple Interest Calculator");
            System.out.println("6. Exit");
            System.out.print("Enter your choice (1-6): ");
            
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            
            switch (choice) {
                case 1:
                    calculateSumProductDifference();
                    break;
                case 2:
                    calculateStudentMarks();
                    break;
                case 3:
                    calculateSquareAndCube();
                    break;
                case 4:
                    calculateDivision();
                    break;
                case 5:
                    calculateSimpleInterest();
                    break;
                case 6:
                    System.out.println("Thank you for using the program!");
                    break;
                default:
                    System.out.println("Invalid choice! Please enter a number between 1 and 6.");
            }
        } while (choice != 6);
        
        scanner.close();
    }

    // Method 1: Accept two numbers and display their sum, product, and difference
    public static void calculateSumProductDifference() {
        System.out.println("\n--- Sum, Product, and Difference Calculator ---");
        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();
        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();
        
        double sum = num1 + num2;
        double product = num1 * num2;
        double difference = num1 - num2;
        
        System.out.println("\nResults:");
        System.out.println("First number: " + num1);
        System.out.println("Second number: " + num2);
        System.out.println("Sum: " + sum);
        System.out.println("Product: " + product);
        System.out.println("Difference: " + difference);
    }

    // Method 2: Accept student's name and marks in three subjects
    public static void calculateStudentMarks() {
        System.out.println("\n--- Student Marks Calculator ---");
        System.out.print("Enter student's name: ");
        String name = scanner.nextLine();
        
        System.out.print("Enter marks in Subject 1: ");
        double marks1 = scanner.nextDouble();
        System.out.print("Enter marks in Subject 2: ");
        double marks2 = scanner.nextDouble();
        System.out.print("Enter marks in Subject 3: ");
        double marks3 = scanner.nextDouble();
        
        double totalMarks = marks1 + marks2 + marks3;
        double average = totalMarks / 3.0;
        
        System.out.println("\nStudent Information:");
        System.out.println("Name: " + name);
        System.out.println("Marks in Subject 1: " + marks1);
        System.out.println("Marks in Subject 2: " + marks2);
        System.out.println("Marks in Subject 3: " + marks3);
        System.out.println("Total Marks: " + totalMarks);
        System.out.println("Average Marks: " + String.format("%.2f", average));
    }

    // Method 3: Read a number and print its square and cube
    public static void calculateSquareAndCube() {
        System.out.println("\n--- Square and Cube Calculator ---");
        System.out.print("Enter a number: ");
        double number = scanner.nextDouble();
        
        double square = number * number;
        double cube = number * number * number;
        
        System.out.println("\nResults:");
        System.out.println("Number: " + number);
        System.out.println("Square: " + square);
        System.out.println("Cube: " + cube);
    }

    // Method 4: Accept two floating-point numbers and calculate their division
    public static void calculateDivision() {
        System.out.println("\n--- Division Calculator ---");
        System.out.print("Enter first floating-point number: ");
        double num1 = scanner.nextDouble();
        System.out.print("Enter second floating-point number: ");
        double num2 = scanner.nextDouble();
        
        if (num2 == 0) {
            System.out.println("Error: Division by zero is not allowed!");
        } else {
            double result = num1 / num2;
            System.out.println("\nResults:");
            System.out.println("First number: " + num1);
            System.out.println("Second number: " + num2);
            System.out.println("Division result: " + String.format("%.4f", result));
        }
    }

    // Method 5: Simple interest calculator
    public static void calculateSimpleInterest() {
        System.out.println("\n--- Simple Interest Calculator ---");
        System.out.print("Enter principal amount: ");
        double principal = scanner.nextDouble();
        System.out.print("Enter rate of interest (in %): ");
        double rate = scanner.nextDouble();
        System.out.print("Enter time period (in years): ");
        double time = scanner.nextDouble();
        
        double simpleInterest = (principal * rate * time) / 100.0;
        double amount = principal + simpleInterest;
        
        System.out.println("\nResults:");
        System.out.println("Principal: " + principal);
        System.out.println("Rate of Interest: " + rate + "%");
        System.out.println("Time Period: " + time + " years");
        System.out.println("Simple Interest: " + String.format("%.2f", simpleInterest));
        System.out.println("Total Amount: " + String.format("%.2f", amount));
    }
}

