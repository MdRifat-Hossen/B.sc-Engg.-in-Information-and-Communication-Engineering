import java.util.Scanner;

class VolumeCalculator {
    public double radius;
    public double side;
    public double cylinderRadius;
    public double cylinderHeight;

    // Method to calculate the volume of a sphere
    public double volumeOfSphere() {
        return (4.0/3.0) * Math.PI * Math.pow(radius, 3);
    }

    // Method to calculate the volume of a cube
    public double volumeOfCube() {
        return Math.pow(side, 3);
    }

    // Method to calculate the volume of a cylinder
    public double volumeOfCylinder() {
        return Math.PI * Math.pow(cylinderRadius, 2) * cylinderHeight;
    }
}
public class lab8_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        VolumeCalculator calculator = new VolumeCalculator();

        // Input radius for sphere
        System.out.print("Enter the radius of the sphere: ");
        calculator.radius = scanner.nextDouble();

        // Input side length for cube
        System.out.print("Enter the side length of the cube: ");
        calculator.side = scanner.nextDouble();

        // Input radius and height for cylinder
        System.out.print("Enter the radius of the cylinder: ");
        calculator.cylinderRadius = scanner.nextDouble();
        System.out.print("Enter the height of the cylinder: ");
        calculator.cylinderHeight = scanner.nextDouble();

        // Calculate and display volumes
        System.out.println("Volume of the sphere: " + calculator.volumeOfSphere());
        System.out.println("Volume of the cube: " + calculator.volumeOfCube());
        System.out.println("Volume of the cylinder: " + calculator.volumeOfCylinder());
    }
}
