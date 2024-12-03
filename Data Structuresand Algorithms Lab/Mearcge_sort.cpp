#include <bits/stdc++.h>
using namespace std;
void marge(int ar[], int l, int mid, int r)
{
    int n1 = mid - l + 1;
    int n2 = r - mid;
    vector<int> L(n1), R(n2);
    // copy the element;
    for (int i = 0; i < n1; i++)
    {
        L[i] = ar[l + i];
    }

    for (int j = 0; j < n2; j++)
    {
        R[j] = ar[mid + 1 + j];
    }
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            ar[k] = L[i];
            i++;
        }
        else
        {
            ar[k] = R[j];
            j++;
        }
        k++;
    }
    // copy the remaing element of L;
    while (i < n1)
    {
        ar[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        ar[k] = R[j];
        j++;
        k++;
    }
}

void margsort(int ar[], int l, int r)
{
    if (l >= r)
    {
        return;
    }
    int mid = (l + r) / 2;
    margsort(ar, l, mid);
    margsort(ar, mid + 1, r);
    marge(ar, l, mid, r);
}

void pritnvector(int ar[])
{
    for (int i = 0; i < 6; i++)
    {
        cout << ar[i] << " ";
    }
    cout << endl;
}
int main()
{
    int n = 6;
    int ar[n] = {12, 11, 13, 5, 6, 7};
    pritnvector(ar);

    margsort(ar, 0, n - 1);
    pritnvector(ar);

    return 0;
}