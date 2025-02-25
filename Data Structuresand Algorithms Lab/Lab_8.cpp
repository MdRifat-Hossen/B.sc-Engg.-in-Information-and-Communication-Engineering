#include <iostream>
#include <vector>
using namespace std;

void findSubsets(vector<int> &set, int targetSum)
{
    int n = set.size();
    int totalSubsets = 1 << n; // 2^n subsets

    cout << "Subsets that sum up to " << targetSum << ":" << endl;

    for (int mask = 0; mask < totalSubsets; mask++)
    {
        vector<int> subset;
        int sum = 0;

        for (int i = 0; i < n; i++)
        {
            if (mask & (1 << i)) // Check if the i-th element is included
            {
                subset.push_back(set[i]);
                sum += set[i];
            }
        }

        if (sum == targetSum)
        {
            cout << "Subset: ";
            for (int num : subset)
            {
                cout << num << " ";
            }
            cout << endl;
        }
    }
}

int main()
{
    vector<int> set = {5, 10, 12, 13, 15, 18};
    int targetSum = 30;

    findSubsets(set, targetSum);
    return 0;
}
