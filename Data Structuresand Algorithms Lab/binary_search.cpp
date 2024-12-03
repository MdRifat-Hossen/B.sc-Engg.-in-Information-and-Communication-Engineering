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
    sort(ar, ar + n);
    int key;
    cin >> key;
    int l = 0;
    int r = n - 1;
    bool flag = false;
    while (l <= r)
    {
        int mid = (l + r) / 2;
        if (ar[mid] == key)
        {
            cout << ar[mid] << endl;
            flag = true;
            break;
        }
        else if (ar[mid] < key)
        {
            l = mid + 1;
        }
        else
        {
            r = mid - 1;
        }
    }
    if (!flag)
    {
        cout << "Not found" << endl;
    }

    return 0;
}