#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    double x[n], y[n];
    for (int i = 0; i < n; i++)
    {
        cin >> x[i];
        cin >> y[i];
    }
    double value;
    cin >> value;
    double result = 0;
    for (int i = 0; i < n; i++)
    {
        double term = y[i];
        for (int j = 0; j < n; j++)
        {
            if (j != i)
            {
                term *= (value - x[j]) / (x[i] - x[j]);
            }
        }
        result += term;
    }
    cout << result << endl;

    return 0;
}