#include <bits/stdc++.h>
using namespace std;
class student
{
public:
    string name;
    int age;
    int roll;
    student(string name, int age, int roll)
    {
        this->name = name;
        this->age = age;
        this->roll = roll;
    }
    void disply()
    {
        cout << name << " " << age << " " << roll << endl;
    }
};
int main()
{
    string name;
    int age;
    int roll;
    cin >> name >> roll >> age;
    student s(name, age, roll);
    s.disply();

    return 0;
}