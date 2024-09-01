#include <bits/stdc++.h>
using namespace std;
class addTwoString
{
public:
    string name1;
    string name2;
    // addTwoString(string name1,string name2){
    //     this->name1=name1;
    //     this->name2=name2;

    // }
    void add()
    {
        string name3;
        name3 = name1 + name2;
        cout << name3 << endl;
    }
};

int main()
{
    addTwoString obj;
    cin >> obj.name1 >> obj.name2;
    obj.add();

    return 0;
}
