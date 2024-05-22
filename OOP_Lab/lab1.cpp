#include <bits/stdc++.h>
using namespace std;
class Traigle
{
public:
    double width;
    double height;
    Traigle(double width, double height)
    {
        this->height = height;
        this->width = width;
    }
    double area()
    {
        return .5 * width * height;
    }
};
int main()
{
    int h, w;
    cout << "Enter the Height and Widgh :" << endl;
    cin >> h >> w;
    Traigle *area = new Traigle(h, w);
    double are1 = area->area();
    cout << "Traigle area is : " << are1 << endl;

    return 0;
}