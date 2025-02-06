#include <bits/stdc++.h>
using namespace std;
class myqueuse
{
public:
    list<int> l;
    void push(int val)
    {
        l.push_back(val);
    }
    void pop()
    {
        l.pop_front();
    }
    int fron()
    {
        return l.front();
    }
    int size()
    {
        return l.size();
    }
    bool empty()
    {
        if (l.size() == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
int main()
{
    myqueuse q;
    int n;
    cin >> n;
    for (int i = 0; i, i < n; i++)
    {
        int x;
        cin >> x;
        q.push(x);
    }
    while (!q.empty())
    {
        cout << q.fron();
        q.pop();
    }

    return 0;
}