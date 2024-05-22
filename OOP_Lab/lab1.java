import java.util.Scanner;

class Traigle {
    public double height;
    public double wight;

    Traigle(double height, double wight) {
        this.height = height;
        this.wight = wight;
    }

    double area() {
        return .5 * height * wight;
    }

}

public class lab1 {
    public static void main(String[] args) {
        Scanner intput = new Scanner(System.in);

        System.out.println("Enter the Height and width: ");
        double h = intput.nextDouble();
        double w = intput.nextDouble();
        Traigle T = new Traigle(h, w);
        double area = T.area();
        System.out.println("This araea of the Traigle is: " + area);
    }

}