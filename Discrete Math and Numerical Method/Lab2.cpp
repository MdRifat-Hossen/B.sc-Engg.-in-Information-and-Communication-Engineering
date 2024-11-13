#include <bits/stdc++.h>
using namespace std;
int main()
{
    int A[3] = {9, 8, 7};
    int B[2] = {1, 2};
    int reletion[3][2];
    cout << sizeof(A) / sizeof(A[0]);
    cout << "Find the relation :" << endl;
    cout << "{";
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            if (A[i] > B[j])
            {
                cout
                    << "(" << A[i] << ","
                    << B[j] << ")"
                    << ",";
            }
        }
    }
    cout << "}" << endl;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            if (A[i] > B[j])
            {
                reletion[i][j] = 1;
            }
            else
            {
                reletion[i][j] = 0;
            }
        }
    }
    cout << "Print the Matrix:" << endl;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cout
                << reletion[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}