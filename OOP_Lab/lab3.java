import java.util.Scanner;

class MaxAndMin {
    int num1, num2;

    MaxAndMin(int num1, int num2) {
        this.num1 = num1;
        this.num2 = num2;
    }

    void ans() {
        if (num1 > num2) {
            System.out.println("Maximum number is: " + num1);
            System.out.println("Minimum number is: " + num2);
        } else if (num1 < num2) {
            System.out.println("Maximum number is: " + num2);
            System.out.println("Minimum number is: " + num1);
        } else {
            System.out.println("Both numbers are equal: " + num1);
        }
    }
}

public class lab3 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter two numbers:");
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        MaxAndMin m = new MaxAndMin(a, b);
        m.ans();

    }
}
