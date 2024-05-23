import java.util.Scanner;

class SumofNumber {
    public int a, b, c;

    SumofNumber(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public int sum() {
        return a + b + c;
    }
}

public class lab2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a, b, c;
        System.out.println("Enter the Number of Three :");
        a = input.nextInt();
        b = input.nextInt();
        c = input.nextInt();

        SumofNumber s = new SumofNumber(a, b, c);
        int ans = s.sum();
        System.out.println("The sum of the Three Number is: " + ans);

    }

}