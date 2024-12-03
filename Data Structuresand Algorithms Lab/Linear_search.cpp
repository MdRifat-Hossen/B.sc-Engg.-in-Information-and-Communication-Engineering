#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int ar[n];

    for (int i = 0; i < n; i++)
    {
        cin >> ar[i];
    }

    int key;
    cin >> key;

    bool found = false;
    for (int i = 0; i < n; i++)
    {
        if (ar[i] == key)
        {
            cout << i << endl;
            found = true;
            break;
        }
    }

    if (!found)
    {
        cout << "-1" << endl;
    }

    return 0;
}
