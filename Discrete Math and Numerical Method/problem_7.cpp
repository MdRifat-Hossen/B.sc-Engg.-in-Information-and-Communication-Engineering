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
    // Create the forward difference table
    double DiffTable[n][n];
    for (int i = 0; i < n; i++)
    {
        DiffTable[i][0] = y[i];
    }
    for (int i = 1; i < n; i++)
    {
        for (int j = n - 1; j > i - 1; j--)
        {
            DiffTable[j][i] = DiffTable[j][i - 1] - DiffTable[j - 1][i - 1];
        }
    }

    cout << endl
         << "BACKWARD DIFFERENCE TABLE" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << x[i];
        for (int j = 0; j <= i; j++)
        {
            cout << " \t " << DiffTable[i][j];
        }
        cout << endl;
    }

    double value;
    cout << "Enter the value to interpolate: ";
    cin >> value;
    double h = x[1] - x[0];
    double u = (value - x[n - 1]) / h;
    double result = y[n - 1];

    double term = 1.0;
    for (int i = 1; i <= n; i++)
    {
        term *= (u + (i - 1)) / i;
        result += term * DiffTable[n - 1][i];
    }
    cout << "Interpolated value at " << value << " is " << result << endl;

    return 0;
}
