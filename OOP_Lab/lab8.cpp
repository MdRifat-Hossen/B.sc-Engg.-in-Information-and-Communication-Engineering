#include <iostream>
#include <cmath>
using namespace std;

class VolumeCalculator
{
public:
    double radius;
    double side;
    double cylinderRadius;
    double cylinderHeight;

    // Method to calculate the volume of a sphere
    double volumeOfSphere()
    {
        return (4.0 / 3.0) * 3.14 * pow(radius, 3);
    }

    // Method to calculate the volume of a cube
    double volumeOfCube()
    {
        return pow(side, 3);
    }

    // Method to calculate the volume of a cylinder
    double volumeOfCylinder()
    {
        return 3.14 * pow(cylinderRadius, 2) * cylinderHeight;
    }
};

int main()
{
    VolumeCalculator calculator;

    // Input radius for sphere
    cout << "Enter the radius of the sphere: ";
    cin >> calculator.radius;

    // Input side length for cube
    cout << "Enter the side length of the cube: ";
    cin >> calculator.side;

    // Input radius and height for cylinder
    cout << "Enter the radius of the cylinder: ";
    cin >> calculator.cylinderRadius;
    cout << "Enter the height of the cylinder: ";
    cin >> calculator.cylinderHeight;

    // Calculate and display volumes
    cout << "Volume of the sphere: " << calculator.volumeOfSphere() << endl;
    cout << "Volume of the cube: " << calculator.volumeOfCube() << endl;
    cout << "Volume of the cylinder: " << calculator.volumeOfCylinder() << endl;

    return 0;
}
