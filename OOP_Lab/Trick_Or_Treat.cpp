#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, M;
        cin >> N >> M;

        vector<int> A(N), B(N);
        for (int i = 0; i < N; ++i)
        {
            cin >> A[i];
        }
        for (int i = 0; i < N; ++i)
        {
            cin >> B[i];
        }

        unordered_map<int, int> candy_remainder_count;
        for (int i = 0; i < N; ++i)
        {
            int remainder = A[i] % M;
            int required_remainder = (M - remainder) % M;
            candy_remainder_count[required_remainder]++;
        }

        int count = 0;
        for (int i = 0; i < N; ++i)
        {
            int remainder = B[i] % M;
            if (candy_remainder_count.find(remainder) != candy_remainder_count.end())
            {
                count += candy_remainder_count[remainder];
            }
        }

        cout << count << endl;
    }
    return 0;
}
