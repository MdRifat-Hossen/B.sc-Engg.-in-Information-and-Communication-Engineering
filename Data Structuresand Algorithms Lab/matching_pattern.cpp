#include <bits/stdc++.h>
using namespace std;

void patternMaching(string text, string pattern)
{
    int n = text.length();
    int m = pattern.length();
    bool found = false;

    // slide the pattern over the text
    for (int i = 0; i <= n - m; i++)
    {
        int j;
        for (j = 0; j < m; j++)
        {
            if (text[i + j] != pattern[j])
            {
                break;
            }
        }
        if (j == m)
        {
            found = true;
            cout << "pattern found at index : " << i << endl;
        }
    }
    if (!found)
    {
        cout << "pattern not found in the text" << endl;
    }
}

int main()
{
    string text, pattern;
    getline(cin, text);
    getline(cin, pattern);

    patternMaching(text, pattern);

    return 0;
}