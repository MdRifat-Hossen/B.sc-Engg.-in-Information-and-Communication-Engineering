// 0/1 knaspce
#include <iostream>
#include <vector>
using namespace std;

int knapsack(int capacity, vector<int> &weights, vector<int> &profits, int n)
{
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    for (int i = 1; i <= n; i++)
    {
        for (int w = 1; w <= capacity; w++)
        {
            if (weights[i - 1] <= w)
            {
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
            }
            else
            {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}

int main()
{
    vector<int> profits = {15, 25, 13, 23};
    vector<int> weights = {2, 6, 12, 9};
    int capacity = 20;
    int n = profits.size();

    int maxProfit = knapsack(capacity, weights, profits, n);
    cout << "Maximum profit: " << maxProfit << endl;

    return 0;
}
