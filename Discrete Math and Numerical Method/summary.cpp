#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int x[n], y[n];
    for (int i = 0; i < n; i++)
    {
        cin >> x[i];
        cin >> y[i];
    }
    double diff[n][n];
    for (int i = 0; i < n; i++)
    {
        diff[i][0] = y[i];
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < n - i; j++)
        {
            diff[j][i] = diff[j - 1][i - 1] - diff[j][i - 1];
        }
    }
    int value;
    cin >> value;
    double h = x[1] - x[0];
    double u = (value - x[0]) / h;
    double result = y[0];
    double terms = 1.0;
    for (int i = 1; i < n; i++)
    {
        terms = terms * (u - (i - 1)) / i;
        result += terms * diff[0][i];
    }
    cout << result << endl;

    return 0;
}