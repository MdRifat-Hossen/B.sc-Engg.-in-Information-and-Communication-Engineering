#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout << "Enter the Number: " << endl;
    cin >> n;
    int A[n];
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    cout << "A = {";
    for (int i = 0; i < n; i++)
    {
        cout << A[i] << " ";
    }
    cout << "}" << endl;
    cout << "A*A : {";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << "(" << A[i] << "," << A[j] << ")";
        }
    }
    cout << "}" << endl;
    cout << "R1 : {";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (A[j] % A[i] == 0)
                cout << "(" << A[i] << "," << A[j] << ")";
        }
    }
    cout << "}" << endl;

    return 0;
}