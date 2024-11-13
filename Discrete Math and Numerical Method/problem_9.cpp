#include <bits/stdc++.h>
using namespace std;
int main()
{
    cout << "Enter the number of data points: ";
    int n;
    cin >> n;
    double x[n], y[n];
    cout << "Enter the data points (x and y):" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << "x[" << i << "] = ";
        cin >> x[i];
        cout << "y[" << i << "] = ";
        cin >> y[i];
    }
    double value;
    cout << "Enter the value to interpolate: ";
    cin >> value;

    double result = 0;

    // Lagrange interpolation
    for (int i = 0; i < n; i++)
    {
        double term = y[i];
        for (int j = 0; j < n; j++)
        {
            if (j != i)
            {
                term = term * (value - x[j]) / (x[i] - x[j]);
            }
        }
        result += term;
    }

    cout << "Interpolated value at x = " << value << " is " << result << endl;
    return 0;
}
