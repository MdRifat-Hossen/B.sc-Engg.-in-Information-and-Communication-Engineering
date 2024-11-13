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
            if (A[i] <= A[j])
                cout << "(" << A[i] << "," << A[j] << ")";
        }
    }
    cout << "}" << endl;

    return 0;
}
// A = {1 2 3 4 }
// A*A : {(1,1)(1,2)(1,3)(1,4)(2,1)(2,2)(2,3)(2,4)(3,1)(3,2)(3,3)(3,4)(4,1)(4,2)(4,3)(4,4)}
// R1 : {(1,1)(1,2)(1,3)(1,4)(2,2)(2,3)(2,4)(3,3)(3,4)(4,4)}