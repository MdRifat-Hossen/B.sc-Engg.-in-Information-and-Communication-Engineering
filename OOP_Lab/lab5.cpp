#include <bits/stdc++.h>
using namespace std;
class matrix
{
private:
    int c, r;
    int m1[100][100], m2[100][100];

public:
    void setMatrix()
    {
        cin >> r >> c;
        m1[r][c], m2[r][c];
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                cin >> m1[i][j];
            }
        }
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                cin >> m2[i][j];
            }
        }
    }

    void print()
    {

        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                cout << m1[i][j] + m2[i][j];
            }
            cout << endl;
        }
    }
};
int main()
{
    matrix obj;
    // obj.setMatrix();
    // obj.print();
    return 0;
}