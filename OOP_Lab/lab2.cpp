#include <iostream>
using namespace std;

class SumOfNumbers
{
private:
    int num1, num2, num3;

public:
    void setNumbers(int a, int b, int c)
    {
        num1 = a;
        num2 = b;
        num3 = c;
    }

    int calculateSum()
    {
        return num1 + num2 + num3;
    }
};

int main()
{
    SumOfNumbers sumObj;
    int a, b, c;

    cout << "Enter three numbers: ";
    cin >> a >> b >> c;

    sumObj.setNumbers(a, b, c);

    int sum = sumObj.calculateSum();

    cout << "The sum of the three numbers is: " << sum << std::endl;

    return 0;
}
