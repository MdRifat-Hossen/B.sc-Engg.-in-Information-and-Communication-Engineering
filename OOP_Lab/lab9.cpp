
// void printPascal(int rows)
// {
//     for (int i = 0; i < rows; i++)
//     {
//         int coef = 1; // Initialize the coefficient for each row

//         for (int space = 1; space <= rows - i; space++)
//             cout << "  ";

//         for (int j = 0; j <= i; j++)
//         {
//             cout << coef << "   ";           // Print the coefficient
//             coef = coef * (i - j) / (j + 1); // Update the coefficient
//         }
//         cout << endl;
//     }
// }

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int r;
    cin >> r;
    for (int i = 0; i < r; i++)
    {
        int c = 1;
        for (int space = 1; space <= r - i; space++)
        {
            cout << " ";
        }
        for (int j = 0; j <= i; j++)
        {
            cout << c << " ";
            c = c * (i - j) / (j + 1);
        }
        cout << endl;
    }

    return 0;
}
