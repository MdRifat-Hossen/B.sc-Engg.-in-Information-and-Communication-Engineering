#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout << "Enter the elemet of point " << endl;
    cin >> n;
    int x[n], y[n];
    for (int i = 0; i < n; i++)
    {
        cout << "x[" << i << "] = " << endl;
        cin >> x[i];
        cout << "y[" << i << "] = " << endl;
        cin >> y[i];
    }
    double diff[n][n];
    for (int i = 1; i <= n; i++)
    {
        diff[i][0] = y[i];
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < n - i; j++)
        {
            diff[i][j] = diff[j + 1][i - 1] - diff[j][i - 1];
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i; j++)
        {
            cout << x[i] << endl;
            cout << "\t" << diff[i][j] << endl;
        }
    }
    return 0;
}