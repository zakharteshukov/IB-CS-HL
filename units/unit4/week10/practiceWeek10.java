import java.util.Scanner;

public class practiceWeek10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        
        do {
            System.out.println("menu");
            System.out.println("1. daysInMonth");
            System.out.println("2. calculator");
            System.out.println("3. debugMissingBreak");
            System.out.println("4. studentPerformance");
            System.out.println("5. shippingCharges");
            System.out.println("6. Exit");
            System.out.print("The choice of thee shall be: ");
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    daysInMonth(scanner);
                    break;
                case 2:
                    calculator(scanner);
                    break;
                case 3:
                    debugMissingBreak(scanner);
                    break;
                case 4:
                    studentPerformance(scanner);
                    break;
                case 5:
                    shippingCharges(scanner);
                    break;
                case 6:
                    System.out.println("Adios!");
                    break;
                default:
                    System.out.println("Invalid choice!");
                            }
        } while (choice != 6);
        
        scanner.close();
    }
    
    public static void daysInMonth(Scanner scanner) {
        System.out.print("Enter month (1-12): ");
        int month = scanner.nextInt();
        int days = 0;
        switch (month) {
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                days = 31;
                System.out.println("31 days");
                break;
            case 4: case 6: case 9: case 11:
                days = 30;
                System.out.println("30 days");
                break;
            case 2:
                days = 28;
                System.out.println("28 or 29 days (February)");
                break;
            default:
                System.out.println("Invalid month!");
        }
    }
    
    // basic calculator with +, -, *, /
    public static void calculator(Scanner scanner) {
        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();
        System.out.print("Enter operator (+, -, *, /): ");
        String operator = scanner.next();
        char op = operator.charAt(0);
        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();
        double result = 0;
        switch (op) {
        case '+':
            result = num1 + num2;
            System.out.println("Result: " + result);
            break;
        case '-':
            result = num1 - num2;
            System.out.println("Result: " + result);
            break;
        case '*':
            result = num1 * num2;
            System.out.println("Result: " + result);
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                System.out.println("Result: " + result);
            } else {
                System.out.println("Error: Division by zero!");
            }
            break;
        default:
            System.out.println("Invalid operator!");
        }
    }
    
    public static void debugMissingBreak(Scanner scanner) {
        System.out.print("Enter number (1-3): ");
        int num = scanner.nextInt();
        switch (num) {
            case 1:
                System.out.println("One");
                break;
            case 2:
                System.out.println("Two");
                break;
            case 3:
                System.out.println("Three");
                break;
            default:
                System.out.println("Invalid");
        }
    }
    
    public static void studentPerformance(Scanner scanner) {
        System.out.print("Entera grade (A, B, C, D, F): ");
        String input = scanner.next();
        String upperInput = input.toUpperCase();
        char grade = upperInput.charAt(0);
        switch (grade) {
            case 'A':
                System.out.println("A stands for average. Now go play Violin.");
                break;
            case 'B':
                System.out.println("YOU ARE ASIAN(!), NOT B-SIAN!");
                break;
            case 'C':
                System.out.println("Go sell fish.");
                break;
            case 'D':
                System.out.println("A D? Explain youself!? The shame you have brought upon our family!");
                break;
            case 'F':
                System.out.println("You are a dissapointament!.");
                break;
            default:
                System.out.println("That is not a grade, you silly goose!");
        }
    }
    
    public static void shippingCharges(Scanner scanner) {
        System.out.print("Enter region code (1, 2, 3): ");
        int region = scanner.nextInt();
        double charge = 0.0;
        
        switch (region) {
        case 1:
            charge = 10.0;
            break;
        case 2:
            charge = 15.0;
            break;
        case 3:
            charge = 20.0;
            break;
        default:
            System.out.println("Invalid region code!");
            return;
        }
        System.out.println("Shipping charge for region " + region + ": $" + charge);
        System.out.println("\nData Table:");
        System.out.println("Region Code | Charge");
        System.out.println("-----------|------");
        System.out.println("     1      | 10");
        System.out.println("     2      | 15");
        System.out.println("     3      | 20");
    }
}
