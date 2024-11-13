#include <bits/stdc++.h>
using namespace std;

int main()
{

    int c, r;
    cin >> r >> c;
    int R1[r][c];
    //  = {
    //     {1, 0, 1},
    //     {1, 0, 0},
    //     {0, 1, 0}};
    int R2[r][c];
    // = {
    //     {1, 0, 1},
    //     {0, 1, 1},
    //     {1, 0, 0}};
    int M1[r][c], M2[r][c];
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> R1[i][j];
        }
    }
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> R2[i][j];
        }
    }
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            M1[i][j] = R1[i][j] | R2[i][j];
            M2[i][j] = R1[i][j] & R2[i][j];
        }
    }
    cout << endl
         << "R1 union R2: " << endl;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cout << M1[i][j] << " ";
        }
        cout << '\n';
    }
    cout << endl
         << "R1 intersect R2: " << endl;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cout << M2[i][j] << " ";
        }
        cout << '\n';
    }
}