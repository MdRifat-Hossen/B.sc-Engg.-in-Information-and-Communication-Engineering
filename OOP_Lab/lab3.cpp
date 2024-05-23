#include <iostream>
using namespace std;

class maxandmin
{
public:
    int num1, num2;

    maxandmin(int num1, int num2)
    {
        this->num1 = num1;
        this->num2 = num2;
    }
    void ans()
    {
        if (num1 > num2)
        {
            cout << "Maximum number is: " << num1 << endl;
            cout << "Minimum number is: " << num2 << endl;
        }
        else if (num1 < num2)
        {
            cout << "Maximum number is: " << num2 << endl;
            cout << "Minimum number is: " << num1 << endl;
        }
        else
        {
            cout << "Both numbers are equal: " << num1 << endl;
        }
    }
};

int main()
{
    int a, b;
    cout << "Enter the number of two:" << endl;
    cin >> a >> b;
    maxandmin *m = new maxandmin(a, b);
    m->ans();

    return 0;
}