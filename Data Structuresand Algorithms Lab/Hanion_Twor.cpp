#include <bits/stdc++.h>
using namespace std;

void toweofhanion(int n, char sourc, char Axuliary, char destitation)
{
    // base case
    if (n == 1)
    {
        cout << "Move disk 1 from " << sourc << " to " << destitation << endl;
        return;
    }
    // Move top n-1 dist from source to axuiliary
    toweofhanion(n - 1, sourc, Axuliary, destitation);

    // move the nth dist from source to destination
    cout << "Move disk" << n << " from " << sourc << " to " << destitation << endl;
    // Move the n-1 disks from the auxialy to distination
    toweofhanion(n - 1, Axuliary, sourc, destitation);
}

int main()
{
    int n;
    cin >> n;
    char sourc, Axuliary, destitation;
    cin >> sourc >> Axuliary >> destitation;
    cout << "Total Moving disk " << (1 << n) - 1 << endl;
    toweofhanion(n, sourc, Axuliary, destitation);
    return 0;
}