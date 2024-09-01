#include <bits/stdc++.h>
using namespace std;
class BannkAcount
{
private:
    string name;
    double balance;

public:
    BannkAcount(string &name, double balance)
    {
        this->name = name;
        this->balance = balance;
    }
    void display()
    {
        cout << "Name : " << name << endl;
        cout << "Balance : $ " << balance << endl;
    }
    void diposit(double amount)
    {
        balance += amount;
        cout << "Diposit $" << amount << " Succesfull" << endl;
    }
    void withdraw(double amount)
    {
        if (balance >= amount)
        {
            balance -= amount;
            cout << "Withdraw of $" << amount << " Successfull" << endl;
        }
        else
        {
            cout << "insuficiant Balance" << endl;
        }
    }
};
int main()
{
    string name;
    double mainBalance, depositBalance, withdraw;

    cout << "Enter the Oner Name" << endl;
    getline(cin, name);
    cout << "Enter the main balance" << endl;
    cin >> mainBalance;

    BannkAcount account(name, mainBalance);
    account.display();
    cout << "Enter the dposit amount " << endl;
    cin >> depositBalance;
    account.diposit(depositBalance);
    cout << "Enter the amount of withdraow" << endl;
    cin >> withdraw;
    account.withdraw(withdraw);
    cout << "account Information " << endl;
    account.display();

    return 0;
}