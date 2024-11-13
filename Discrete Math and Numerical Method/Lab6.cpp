#include <bits/stdc++.h>
using namespace std;

#define order 4
#define MAXN 100
int main()
{

    int n;
    cin >> n;
    float x[MAXN + 1], y[MAXN + 1];
    for (int i = 0; i <= n; i++)
        cin >> x[i] >> y[i];

    float value;
    cin >> value;

    float diff[MAXN + 1][order + 1];
    for (int i = 0; i <= n - 1; i++)
        diff[i][1] = y[i + 1] - y[i];

    for (int j = 2; j <= order; j++)
    {
        for (int i = 0; i <= n - j; i++)
        {
            diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1];
        }
    }
    int idx = 0;
    while (x[idx] < value)
        idx++;
    idx--;

    float h = x[1] - x[0];
    float u = (value - x[idx]) / h;

    float y_value = y[idx];

    float fact_u = 1.0, multi = 1.0;
    for (int i = 1; i <= order; i++)
    {
        fact_u *= u - i + 1;
        multi *= i;
        y_value += (fact_u / multi) * diff[idx][i];
    }
    cout << y_value << endl;
}
/*
5
1931 12
1941 15
1951 20
1961 27
1971 39
1981 52
1934

3
45 0.7071
50 0.7660
55 0.8192
60 0.8660
52


6
100 10.63
150 13.03
200 15.04
250 16.81
300 18.42
350 19.90
400 21.27
218
*/